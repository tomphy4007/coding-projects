import pygame
import pyaudio
import numpy as np
import wave
import os
from tkinter import Tk, filedialog

pygame.init()

WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("V-Z-2008")
ico_path = os.path.join(os.path.dirname(__file__), "yes.ico")
icon_surface = pygame.image.load(ico_path)
pygame.display.set_icon(icon_surface)

root = Tk()
root.withdraw()
audio_path = filedialog.askopenfilename(title="Select an audio file", filetypes=[("Audio Files", "*.wav;*.mp3")])
root.destroy()

if not audio_path:
    print("No file selected. Exiting.")
    exit()

if not audio_path.lower().endswith(".wav"):
    print("Please select a WAV file. Exiting.")
    exit()

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100

p = pyaudio.PyAudio()

audio_stream = p.open(format=FORMAT,
                      channels=CHANNELS,
                      rate=RATE,
                      output=True)

def get_audio_data():
    wf = wave.open(audio_path, 'rb')
    data = wf.readframes(CHUNK)
    while data:
        yield data
        data = wf.readframes(CHUNK)
    wf.close()

def polar_to_cartesian(r, theta):
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return int(x), int(y)

def get_gradient_color(magnitude):
    color1 = (0, 0, 0)
    color2 = (32, 32, 32)
    r = np.interp(magnitude, [0, 1], [color1[0], color2[0]])
    g = np.interp(magnitude, [0, 1], [color1[1], color2[1]])
    b = np.interp(magnitude, [0, 1], [color1[2], color2[2]])
    return int(r), int(g), int(b)

running = True
audio_data = get_audio_data()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.w, event.h
            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

    try:
        data = next(audio_data)
        audio_stream.write(data)
    except StopIteration:
        running = False

    numpy_data = np.frombuffer(data, dtype=np.int16)
    fft_data = np.fft.fft(numpy_data)
    freqs = np.fft.fftfreq(len(fft_data), 1.0 / RATE)
    freqs = freqs[:len(freqs) // 2]
    fft_data = np.abs(fft_data[:len(fft_data) // 2]) / (25 * CHUNK)
    screen.fill((255, 255, 255))
    center_x, center_y = WIDTH // 2, HEIGHT // 2
    max_radius = min(center_x, center_y) - 4
    boundary_radius = max_radius - 10  


    for i, freq in enumerate(freqs):
        angle = i / len(freqs) * 50 * np.pi
        radius = max_radius * fft_data[i]
        x, y = polar_to_cartesian(radius, angle)
        color = get_gradient_color(fft_data[i])
        
        if radius <= boundary_radius:
            pygame.draw.circle(screen, color, (center_x + x, center_y + y), 3)

            if i > 0:
                prev_x, prev_y = polar_to_cartesian(max_radius * fft_data[i - 1], (i - 1) / len(freqs) * 50 * np.pi)
                if prev_x ** 2 + prev_y ** 2 <= boundary_radius ** 2:
                    pygame.draw.line(screen, color, (center_x + prev_x, center_y + prev_y), (center_x + x, center_y + y), 2)

    pygame.display.flip()

audio_stream.stop_stream()
audio_stream.close()
p.terminate()
pygame.quit()
