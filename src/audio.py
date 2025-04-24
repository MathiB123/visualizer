from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np


# sample_rate, data = wavfile.read(r"src/music_sounds/cat.wav")

# # print(data.dtype) => format wav
# # wavfile.write(r"src/music_sounds/.wav", sample_rate, data)



# duration = len(data)/sample_rate
# times = np.arange(0, duration, 1/sample_rate)

# # data[:, 0] => gauche, data[:, 1] => droite, c'est stéréo

# plt.rcParams["figure.figsize"] = (10, 5)
# plt.plot(times, data[:, 0], label="Gauche")
# plt.plot(times, data[:, 1], label="Droite")
# plt.xlabel("Time (s)")
# plt.ylabel("Amplitude")
# plt.legend()
# plt.show()

# times = np.arange(0, 3, 1/48000)
# data_1 = np.cos(2*np.pi*440*times, dtype=np.float32)

# wavfile.write(r"src/music_sounds/aaa.wav", 48000, data_1)

# plt.plot(times, data)
# plt.show()


n = np.arange(1, 15)
r_n = 4/(np.pi * n)
theta_n = np.where(n % 2 == 0, np.pi, 0)

plt.stem(n, theta_n, basefmt="black")
plt.xlabel("n")
plt.ylabel("theta_n")
plt.xticks(n)
plt.show()
