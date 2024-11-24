import numpy as np
import matplotlib.pyplot as plt

#COSINUS, SINUS
# x_s = np.linspace(0,2*np.pi, 100)
# sin_s = np.sin(2*x_s)
# cos_s = np.cos(2*x_s)

# plt.scatter(x_s, sin_s, label="sin")
# plt.scatter(x_s, cos_s, label="cos")
# plt.grid()
# plt.legend()
# plt.show()

#EXEMPLE SÉRIE DE FOURIER DENTS DE SCIE
# A = 1
# L = 1
# N = 1000 #Dans la somme
# m = 500 #Nb de points 

# x_s = np.linspace(-1, 1, m)

# f = np.zeros(x_s.shape)

# for i in range(N):
#     values = (1/(np.pi*(i+1)))*np.sin(2*np.pi*(i+1)*x_s)
#     sign = (-1)**(i+2)
#     f += sign*values

# plt.plot(x_s, f)
# plt.grid()
# plt.show()