import pygame
import pyaudio
import numpy as np


pygame.init()


WIDTH, HEIGHT = 100, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Circular Audio Visualizer")


CHUNK = 1000
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)


def polar_to_cartesian(r, theta):
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return int(x), int(y)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    data = stream.read(CHUNK)
    numpy_data = np.frombuffer(data, dtype=np.int16)
    fft_data = np.fft.fft(numpy_data)
    freqs = np.fft.fftfreq(len(fft_data), 10.0 / RATE)
    freqs = freqs[:len(freqs)//2]
    fft_data = np.abs(fft_data[:len(fft_data)//2]) / (20 * CHUNK)
    screen.fill((43, 240, 0))
    center_x, center_y = WIDTH // 2, HEIGHT // 2
    max_radius = min(center_x, center_y) - 4

    for i, freq in enumerate(freqs):
        
        angle = i / len(freqs) * 40 * np.pi
        radius = max_radius * fft_data[i]
        x, y = polar_to_cartesian(radius, angle)
        pygame.draw.circle(screen, (0, 0, 255), (center_x + x, center_y + y), 3)

    pygame.display.flip()

stream.stop_stream()
stream.close()
p.terminate()
pygame.quit()
