"""
Comparison between various random data traces and the SketchMin result.
"""

from computing import *
from distribution import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.mlab import griddata


fig1 = plt.figure()
ax1 = fig1.add_subplot(111, projection='3d')
fig2 = plt.figure()
ax2 = fig2.add_subplot(111, projection='3d')

# Standart deviation 
fig3 = plt.figure()
ax3 = fig3.add_subplot(111, projection='3d')

size = 10000
u = 100
eps = 0.1
delta = 0.001

print("Starting generation")

data0 = entry_uniform(size, u)
data1 = entry_zipfian(size, u, 2)
data2 = entry_zipfian(size, u, 3)
data3 = entry_zipfian(size, u, 4)
data4 = entry_zipfian(size, u, 5)
data5 = entry_zipfian(size, u, 6)
data6 = entry_poisson(size, u, u/(2**1))
data7 = entry_poisson(size, u, u/(2**2))
data8 = entry_poisson(size, u, u/(2**3))
data9 = entry_poisson(size, u, u/(2**4))
data10 = entry_poisson(size, u, u/(2**5))
data11 = entry_binomial(size, u, 0.42)
data12 = entry_negative_binomial(size, u, 0.42)

print("Ending generation")


def print_data(data):
    """
    Print distribution of a list.
    :param data: List of integers.
    """
    data_array = np.array([e for e in data])
    plt.hist(data_array)
    plt.show()
    return None


DATA_elts = [globals()['data' + str(i)] for i in range(13)]
DATA_freq = [freq_vect(DATA_elts[i], u+1) for i in range(13)]


# SKETCH MIN RESULTS

print('Starting computing sketchmin codeviance matrix')

nb_tests = 10

cod_full_matrix = np.array([[[0. for k in range(nb_tests)] for i in range(13)]
                            for j in range(13)], dtype=float)
for k in range(nb_tests):
    cod_matrix = codeviance_all_streams(DATA_elts, eps, delta, u)
    for i in range(13):
        for j in range(13):
            cod_full_matrix[i, j, k] = cod_matrix[i, j]
            
cod_matrix = np.array([[average(cod_full_matrix[i, j]) for i in range(13)]
                      for j in range(13)], dtype=float)
                            
stdev_matrix = np.array([[stdev(cod_full_matrix[i, j]) for i in range(13)]
                        for j in range(13)], dtype=float)

print('Ending computing sketchmin codeviance matrix')

# REAL CODEVIANCE MATRIX

print('Starting computing accurate codeviance matrix')

cod_real_matrix = np.array([[0. for i in range(13)] for j in range(13)],
                           dtype=float)

for i in range(13):
        for j in range(i, 13):
            cod = codeviance(DATA_freq[i], DATA_freq[j])
            cod_real_matrix[i, j] = cod
            cod_real_matrix[j, i] = cod

print('Ending computing accurate codeviance matrix')

# PLOTTING in 3D

print('Starting plotting')

Xi = np.array([i for i in range(13)])
Yi = np.array([i for i in range(13)])

x = np.array([j for i in range(13) for j in range(13)])
y = np.array([i for i in range(13) for j in range(13)])

# Real
z1 = np.array([cod_real_matrix[i, j] for i in range(13) for j in range(13)])

# Sketch min
z2 = np.array([cod_matrix[i, j] for i in range(13) for j in range(13)])

# Standard deviation
z3 = np.array([stdev_matrix[i, j] for i in range(13) for j in range(13)])
               
X, Y = np.meshgrid(Xi, Yi)

Z1 = griddata(x, y, z1, X, Y, interp='linear')
Z2 = griddata(x, y, z2, X, Y, interp='linear')
Z3 = griddata(x, y, z3, X, Y, interp='linear')

ax1.plot_surface(X, Y, Z1, rstride=1, cstride=1, color='g')
ax2.plot_surface(X, Y, Z2, rstride=1, cstride=1, color='r')
ax3.plot_surface(X, Y, Z3, rstride=1, cstride=1, color='b')
plt.show()

print(cod_matrix)
