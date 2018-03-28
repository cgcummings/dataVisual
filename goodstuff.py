from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as sp
fig = plt.figure()
ax = fig.gca(projection='3d')
a = 0.22361
b = 1.6
sigma =41.88
const = sigma / (4.0 * np.pi * sp.epsilon_0)

 
x, y, z = np.meshgrid(np.arange(0.01, a, .1),
                      np.arange(0.01, b, .1),
                      np.arange(0.01, 0.4, .1))


u = const * np.log(((np.sqrt((x - a) ** 2 + y ** 2 + z ** 2) + y) 
				/ (np.sqrt((x - a) ** 2 + (y - b) ** 2 + z ** 2) + y - b)) 
				/ ((np.sqrt(x ** 2 + y ** 2 + z ** 2) + y) 
				/ (np.sqrt(x ** 2 + (y - b) ** 2 + z ** 2) + y - b)))



v = const * np.log(((np.sqrt(x ** 2 + (y - b) ** 2 + z ** 2) + x) 
				/ (np.sqrt((x - a) ** 2 + (y - b) ** 2 + z ** 2) + x - a)) 
				/ ((np.sqrt(x ** 2 + y ** 2 + z ** 2) + x) 
				/ (np.sqrt((x - a) ** 2 + y ** 2 + z ** 2) + x - a)))

w = const *  ((x - a) * np.log((np.sqrt((x - a) ** 2 + (y - b) ** 2 + z ** 2) + y - b) / (np.sqrt((x - a) ** 2 + y ** 2 + z ** 2) + y))
				+ x * np.log((np.sqrt(x ** 2 + y ** 2 + z ** 2) + y) / (np.sqrt(x ** 2 + (y - b) ** 2 + z ** 2) + y - b))
				+ (y - b) * np.log((np.sqrt((x - a) ** 2 + (y - b) ** 2 + z ** 2) + x - a) / (np.sqrt(x ** 2 + (y - b) ** 2 + z ** 2) + x))
				+ y * np.log((np.sqrt(x ** 2 + y ** 2 + z ** 2) + x)/ (np.sqrt((x - a) ** 2 + y ** 2 + z ** 2) + x - a))
				+ z * (np.arctan(y * (x - a) / (z * np.sqrt((x - a) ** 2 + y ** 2 + z ** 2)))
					+ np.arctan((y - b) * x / (z * np.sqrt(x ** 2 + (y - b) ** 2 + z ** 2)))
					- np.arctan(x * y / (z * np.sqrt(x ** 2 + y ** 2 + z ** 2)))
					- np.arctan((x - a) * (y - b) / (z * np.sqrt((x - a) ** 2 + (y - b) ** 2 + z ** 2)))))







ax.quiver(x, y, z, u, v, w)
plt.show()
##single point perspective##
