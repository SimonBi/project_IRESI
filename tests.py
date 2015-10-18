from computing import *
import extract_sdschttp as sdsc
import extract_epahttp as epa
import extract_calgaryaccess as calga


X = [randint(0, 50) for i in range(50)]
Y = [randint(0, 50) for i in range(50)]
Z = [randint(0, 50) for i in range(50)]

u = 50
eps = 0.01
delta = 0.0001

DATA = [X, Y,Z]

cod_matrix = codeviance_all_streams(DATA, eps, delta, u)
print(cod_matrix)


#data_stream = calga.extract_filename()
#data_stream = calga.extract_sources()
data_stream = epa.extract_sources()
#data_stream = sdsc.extract_sources(1)
#data_stream = sdsc.extract_sources(2)

#print(data_stream)
print(len(data_stream))
