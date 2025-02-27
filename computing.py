from hashing import *
from codeviance import *


def min_vect(l):
    """Return the minimum element of l"""

    n = len(l)
    if n == 0:
        return "Error min"
    elif n == 1:
        return l[0]
    else:
        x = min_vect(l[1::])
        if l[0] < x:
            return l[0]
        else:
            return x
      

def codeviance_two_streams(data1, data2, t, k, u):
    """Return the codeviance between two streams"""
    
    hash_f = choosehashfunctions(t)
    
    repartition1 = partition(data1, t, k, u, hash_f)
    repartition2 = partition(data2, t, k, u, hash_f)
    
    cod_vect = np.array([0. for _ in range(t)], dtype=float)
    
    for i in range(t):
        cod = codeviance(repartition1[i], repartition2[i])
        cod_vect[i] = cod
    
    return min_vect(cod_vect)
    
    
def codeviance_all_streams(data, eps, delta, u):
    """
    Return the codeviance matrix
    :param data: Array of streams.
    """
    
    n = len(data)
    cod_matrix = np.array([[0. for _ in range(n)] for _ in range(n)],
                          dtype=float)
    
    t = int(np.ceil(np.log(1 / delta)))
    k = int(np.ceil(1 / eps))
    
    for i in range(n):
        for j in range(i, n):
            cod = codeviance_two_streams(data[i], data[j], t, k, u)
            cod_matrix[i, j] = cod
            cod_matrix[j, i] = cod
    
    return cod_matrix
    
    
def freq_vect(x, u):
    """
    Return the frequency vector or the list x
    which values are integers between O and u
    :rtype: Array of integers.
    """
    x_res = np.array([0 for _ in range(u+1)])
    for e in x:
        x_res[e] += 1
    return x_res
