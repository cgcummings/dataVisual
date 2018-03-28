import numpy as np
import scipy.constants as sp 
import seaborn as sns
import matplotlib.pyplot as plt
import time
from numba import jit

a = 0.22361
b = 1.6
sigma = 41.88

@jit
def e_field(x, y, z):
	e_at_pt = np.empty(3)
	const = sigma / (4.0 * np.pi * sp.epsilon_0)

	e_at_pt[0] = const * np.log(((np.sqrt((x - a) ** 2 + y ** 2 + z ** 2) + y) 
				/ (np.sqrt((x - a) ** 2 + (y - b) ** 2 + z ** 2) + y - b)) 
				/ ((np.sqrt(x ** 2 + y ** 2 + z ** 2) + y) 
				/ (np.sqrt(x ** 2 + (y - b) ** 2 + z ** 2) + y - b)))

	e_at_pt[1] = const * np.log(((np.sqrt(x ** 2 + (y - b) ** 2 + z ** 2) + x) 
				/ (np.sqrt((x - a) ** 2 + (y - b) ** 2 + z ** 2) + x - a)) 
				/ ((np.sqrt(x ** 2 + y ** 2 + z ** 2) + x) 
				/ (np.sqrt((x - a) ** 2 + y ** 2 + z ** 2) + x - a)))

	e_at_pt[2] = const * (
				(x - a) * np.log((np.sqrt((x - a) ** 2 + (y - b) ** 2 + z ** 2) + y - b) / (np.sqrt((x - a) ** 2 + y ** 2 + z ** 2) + y))
				+ x * np.log((np.sqrt(x ** 2 + y ** 2 + z ** 2) + y) / (np.sqrt(x ** 2 + (y - b) ** 2 + z ** 2) + y - b))
				+ (y - b) * np.log((np.sqrt((x - a) ** 2 + (y - b) ** 2 + z ** 2) + x - a) / (np.sqrt(x ** 2 + (y - b) ** 2 + z ** 2) + x))
				+ y * np.log((np.sqrt(x ** 2 + y ** 2 + z ** 2) + x)/ (np.sqrt((x - a) ** 2 + y ** 2 + z ** 2) + x - a))
				+ z * (np.arctan(y * (x - a) / (z * np.sqrt((x - a) ** 2 + y ** 2 + z ** 2)))
					+ np.arctan((y - b) * x / (z * np.sqrt(x ** 2 + (y - b) ** 2 + z ** 2)))
					- np.arctan(x * y / (z * np.sqrt(x ** 2 + y ** 2 + z ** 2)))
					- np.arctan((x - a) * (y - b) / (z * np.sqrt((x - a) ** 2 + (y - b) ** 2 + z ** 2)))))

	E = np.sqrt(e_at_pt[0] ** 2 + e_at_pt[1] ** 2 + e_at_pt[2] ** 2)

	return E

x = np.linspace(0, a, 100)
y = np.linspace(0, b, 100)
z = 0.030

E = np.zeros((len(x), len(y)))

for ii in range(len(x)):
	for jj in range(len(y)):
		E[ii,jj] = e_field(x[ii], y[jj], z)


fig = plt.contourf(x, y,E)
cbar = plt.colorbar(fig)

plt.show()









