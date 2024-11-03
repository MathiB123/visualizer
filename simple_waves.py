import numpy as np
import matplotlib.pyplot as plt

x_s = np.linspace(0,2*np.pi, 100)
sin_s = np.sin(2*x_s)
cos_s = np.cos(2*x_s)

plt.scatter(x_s, sin_s)
plt.scatter(x_s, cos_s)
plt.plot(x_s, [1]*len(x_s), color = "black")
plt.plot(x_s, [0]*len(x_s), color = "black")
plt.plot(x_s, [-1]*len(x_s), color = "black")
plt.show()
