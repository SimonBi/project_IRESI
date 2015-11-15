"""
Comparison between the real data traces and the SketchMin algorithm result.
"""


from computing import *
from traces_extraction import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.mlab import griddata


fig1 = plt.figure()
ax1 = fig1.add_subplot(111, projection='3d')
fig2 = plt.figure()
ax2 = fig2.add_subplot(111, projection='3d')

eps = 0.001
delta = 0.001

data, u = extract_all_traces()
nb_data = len(data)


def print_data(d):
    """
    Print distribution of a list.
    :param d: List of integers.
    """
    data_array = np.array([e for e in d])
    plt.hist(data_array)
    plt.show()


DATA_freq = [freq_vect(data[i], u+1) for i in range(nb_data)]


# SKETCH MIN RESULTS

print('Starting computing sketchmin codeviance matrix')

cod_matrix = codeviance_all_streams(data, eps, delta, u)

print('Ending computing sketchmin codeviance matrix')

# REAL CODEVIANCE MATRIX

print('Starting computing accurate codeviance matrix')

cod_real_matrix = np.array([[0. for i in range(nb_data)]
                            for j in range(nb_data)], dtype=float)

for i in range(nb_data):
        for j in range(i, nb_data):
            cod = codeviance(DATA_freq[i], DATA_freq[j])
            cod_real_matrix[i, j] = cod
            cod_real_matrix[j, i] = cod

print('Ending computing accurate codeviance matrix')

# PLOTTING in 3D

print('Starting plotting')

Xi = np.array([i for i in range(nb_data)])
Yi = np.array([i for i in range(nb_data)])

x = np.array([j for i in range(nb_data) for j in range(nb_data)])
y = np.array([i for i in range(nb_data) for j in range(nb_data)])

# Real
z1 = np.array([cod_real_matrix[i, j] for i in range(nb_data)
               for j in range(nb_data)])

# Sketch min
z2 = np.array([cod_matrix[i, j] for i in range(nb_data)
               for j in range(nb_data)])

# Log scale
mini = min_vect(z1)
for k in range(nb_data**2):
    z1[k] = np.log(z1[k] + abs(mini) + 1)
mini = min_vect(z2)
for k in range(nb_data**2):
    z2[k] = np.log(z2[k] + abs(mini) + 1)

X, Y = np.meshgrid(Xi, Yi)

Z1 = griddata(x, y, z1, X, Y, interp='linear')
Z2 = griddata(x, y, z2, X, Y, interp='linear')

ax1.plot_surface(X, Y, Z1, rstride=1, cstride=1, color='g')
ax2.plot_surface(X, Y, Z2, rstride=1, cstride=1, color='r')
plt.show()

print('Ending plotting')
