import numpy as np
import matplotlib.pyplot as plt
import pyaudio
import threading

class AudioVisualizer:
    def __init__(self):
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.audio_data = np.zeros(self.CHUNK)
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.ax.set_xlim(0, self.CHUNK)
        self.ax.set_ylim(0, 255)
        self.ax.set_zlim(0, 1000)
        self.ax.set_xlabel('Frequency (Hz)')
        self.ax.set_ylabel('Time')
        self.ax.set_zlabel('Amplitude')
        self.stream = None
        self.running = False

    def start_audio_stream(self):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format=self.FORMAT,
            channels=self.CHANNELS,
            rate=self.RATE,
            input=True,
            output=True,
            frames_per_buffer=self.CHUNK
        )
        self.running = True
        threading.Thread(target=self.update_plot).start()

    def update_plot(self):
        while self.running:
            data = self.stream.read(self.CHUNK, exception_on_overflow=False)
            data_int = np.frombuffer(data, dtype=np.int16)
            self.audio_data = np.abs(np.fft.fft(data_int))
            self.audio_data = self.audio_data[:self.CHUNK]
            self.ax.clear()
            self.ax.plot(np.arange(self.CHUNK), self.audio_data, zs=0, zdir='y')
            plt.pause(0.01)

    def stop_audio_stream(self):
        self.running = False
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
        self.p.terminate()

if __name__ == "__main__":
    visualizer = AudioVisualizer()
    visualizer.start_audio_stream()
    plt.show()
    visualizer.stop_audio_stream()
