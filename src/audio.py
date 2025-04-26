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




# w = np.linspace(-5, 5, 1000)
# y = (10/w)*np.sin(3*w/2)
# plt.plot(w, np.abs(y))
# plt.xlabel("w")
# plt.ylabel("r(w)")
# plt.xticks(np.arange(-5, 6))
# plt.yticks([0.0, 2.5, 5.0, 7.5, 10.0, 12.5, 15.0])
# plt.show()

from scipy.integrate import quad

x_s = np.linspace(-5, 5, 1000)
rect = np.zeros_like(x_s, float)
b = 100
factor = 10/np.pi

for i, x in enumerate(x_s):
    rect[i] = quad(lambda w: factor * np.sin(3*w/2) * np.cos(w*x)/w, 0, b)[0]


plt.plot(x_s, rect)
plt.xlabel("x")
plt.ylabel("Rect(x)")
plt.xticks(np.arange(-5, 6))
plt.show()