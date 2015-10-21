from computing import *
from traces_extraction import *



#X = [randint(0, 50) for i in range(50)]
#Y = [randint(0, 50) for i in range(50)]
#Z = [randint(0, 50) for i in range(50)]

#u = 50


#DATA = [X, Y,Z]

#cod_matrix = codeviance_all_streams(DATA, eps, delta, u)
#print(cod_matrix)


## FINAL TESTS

eps = 0.1
delta = 0.0001

data1_dic = extract_entries('1')
data2_dic = extract_entries('22')
data3_dic = extract_entries('22')
data4_dic = extract_entries('22')


u = max (data1_dic['max'], data2_dic['max'])

DATA = [data1_dic['elements'], data2_dic['elements']]

cod_matrix = codeviance_all_streams(DATA, eps, delta, u)
print(cod_matrix)

data1 = np.array([e for e in data1_dic['elements']])
data2 = np.array([e for e in data2_dic['elements']])

print(codeviance(data1, data1))
#print(codeviance(data1, data2)) -> prob not yet solved
print(codeviance(data2, data2))


