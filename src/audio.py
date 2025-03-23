from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np


sample_rate, data = wavfile.read(r"src/music_sounds/allo.wav")

# print(data.dtype) => format wav
# wavfile.write(r"src/music_sounds/allo_reversed.wav", sample_rate, data[::-1, :])

duration = len(data)/sample_rate
times = np.arange(0, duration, 1/sample_rate)

# data[:, 0] => gauche, data[:, 1] => droite, c'est stéréo
plt.rcParams["figure.figsize"] = (10, 5)
plt.plot(times, data[:, 0], label="Gauche")
plt.plot(times, data[:, 1], label="Droite")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.show()
