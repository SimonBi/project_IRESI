from computing import *
from traces_extraction import *
from distribution import *
import matplotlib.pyplot as plt


size = 1000
u = 200
eps = 0.01
delta = 0.0001


data0 = extract_entries('', True, entry_uniform(size,u))['elements']
data1 = extract_entries('', True, entry_zipfian(size,u,2))['elements']
data2 = extract_entries('', True, entry_zipfian(size,u,3))['elements']
data3 = extract_entries('', True, entry_zipfian(size,u,4))['elements']
data4 = extract_entries('', True, entry_zipfian(size,u,5))['elements']
data5 = extract_entries('', True, entry_zipfian(size,u,6))['elements']
data6 = extract_entries('', True, entry_poisson(size,u, u/(2**1)))['elements']
data7 = extract_entries('', True, entry_poisson(size,u, u/(2**2)))['elements']
data8 = extract_entries('', True, entry_poisson(size,u, u/(2**3)))['elements']
data9 = extract_entries('', True, entry_poisson(size,u, u/(2**4)))['elements']
data10 = extract_entries('', True, entry_poisson(size,u, u/(2**5)))['elements']
data11 = extract_entries('', True, entry_binomial(size,u, 0.42))['elements']
data12 = extract_entries('', True, entry_negative_binomial(size,u, 0.42))['elements']


## PRINT DISTRIBUTION

def print_data(data):
    data_array = np.array([e for e in data])
    plt.hist(data_array)
    plt.show()

print_data(data0)



#DATA = [globals()['data' + str(i)] for i in range(13)]


### SKECH MIN RESULTS

#cod_matrix = codeviance_all_streams(DATA, eps, delta, u)

### REAL CODEVIANCE MATRIX

#cod_real_matrix = np.array([[0. for i in range(13)] for j in range(13)], dtype=float)
#for i in range(13):
        #for j in range(i,13):
            #cod = codeviance(DATA[i], DATA[j])
            #cod_real_matrix[i,j] = cod
            #cod_real_matrix[j,i] = cod
