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



# t = np.arange(0, 11.5, 0.5)
# sin = np.sin(t)

# plt.stem(t, sin, basefmt="black")
# plt.xlabel("x")
# plt.xticks(np.arange(0, 12))
# plt.ylabel("sin(x)")
# plt.show()


# t = np.arange(0, 1, 1/100000)
# samples = np.arange(0,1, 1/16)
# two_hz = np.sin(2*np.pi*2*t)
# two_hz_samples = np.sin(2*np.pi*2*samples)
# eighteen_hz = np.sin(-1*2*np.pi*30*t)
# eighteen_hz_samples = np.sin(-1*2*np.pi*30*samples)
# plt.plot(t, two_hz, label="Signal complet")
# plt.scatter(samples, two_hz_samples, c="black")
# plt.plot(t, eighteen_hz, label="Signal complet", c="orange")
# plt.scatter(samples, eighteen_hz_samples, c="black", label="Échantillons")
# plt.xlabel("Temps (s)")
# # plt.ylabel("Signal à 2Hz")
# # plt.ylabel("Signal à 18Hz")
# plt.ylabel("Superposition des signaux")
# plt.legend(loc="upper right")
# plt.show()



# x = np.arange(-20, 20, 1)
# y = np.zeros_like(x)

# for i,x_i in enumerate(x):
#     if x_i in [-18, -14, -2, 2, 14, 18]:
#         print(i)
#         y[i] = 1


# plt.stem(x,y)
# plt.xticks([-18, -16, -14, -2, 0, 2, 14, 16, 18])
# plt.yticks([])
# plt.xlabel("Fréquences (Hz)")
# plt.show()



