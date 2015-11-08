from computing import *
from traces_extraction import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.mlab import griddata
fig1 = plt.figure()
ax1 = fig1.add_subplot(111, projection='3d')
fig2 = plt.figure()
ax2 = fig2.add_subplot(111, projection='3d')


# X = [randint(0, 50) for i in range(50)]
# Y = [randint(0, 50) for i in range(50)]
# Z = [randint(0, 50) for i in range(50)]

# u = 50


# DATA = [X, Y,Z]

# cod_matrix = codeviance_all_streams(DATA, eps, delta, u)
# print(cod_matrix)


# FINAL TESTS

eps = 0.1
delta = 0.0001

datas, u = extract_all_traces()
# for data in range(len(datas)):
#     globals()['data'+str(data)+'_dic'] = datas[data]
# data1_dic = extract_entries('1')
# data2_dic = extract_entries('22')
# data3_dic = extract_entries('22')
# data4_dic = extract_entries('3')
nb_data = len(datas)


# u = max (data1_dic['max'], data2_dic['max'])
#
# DATA = [data1_dic['elements'], data2_dic['elements']]
#
# cod_matrix = codeviance_all_streams(DATA, eps, delta, u)
# print(cod_matrix)
#
# data1 = np.array([e for e in data1_dic['elements']])
# data2 = np.array([e for e in data2_dic['elements']])
#
# print(codeviance(data1, data1))
# #print(codeviance(data1, data2)) -> prob not yet solved
# print(codeviance(data2, data2))


# PRINT DISTRIBUTION

def print_data(d):
    data_array = np.array([e for e in d])
    plt.hist(data_array)
    plt.show()
    return None

# print_data(data0['elements'])


DATA_elts = datas[:]
# [globals()['data' + str(i) + '_dic'] for i in range(nb_data)]
DATA_freq = [freq_vect(DATA_elts[i], u+1) for i in range(nb_data)]


# SKECH MIN RESULTS

print('Starting computing sketchmin codeviance matrix')

cod_matrix = codeviance_all_streams(DATA_elts, eps, delta, u)

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
# mini = min_vect(z1)
# for k in range(169):
#        z1[k] = np.log(z1[k] + abs(mini) + 1)

# Sketch min
z2 = np.array([cod_matrix[i, j] for i in range(nb_data)
               for j in range(nb_data)])
# mini = min_vect(z2)
# for k in range(169):
#        z2[k] = np.log(z2[k] + abs(mini) + 1)

X, Y = np.meshgrid(Xi, Yi)

Z1 = griddata(x, y, z1, X, Y, interp='linear')
Z2 = griddata(x, y, z2, X, Y, interp='linear')

ax1.plot_surface(X, Y, Z1, rstride=1, cstride=1, color='g')
ax2.plot_surface(X, Y, Z2, rstride=1, cstride=1, color='r')
plt.show()

print('Ending plotting')
