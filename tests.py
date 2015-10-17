from computing import *


X = [randint(0, 50) for i in range(50)]
Y = [randint(0, 50) for i in range(50)]
Z = [randint(0, 50) for i in range(50)]

u = 50
eps = 0.01
delta = 0.0001

DATA = [X, Y,Z]

cod_matrix = codeviance_all_streams(DATA, eps, delta, u)
print(cod_matrix)
