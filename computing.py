import numpy as np

from hashing import *
from codeviance import *


def min_vect(l):
    '''Return the minimum element of l'''
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
            

def codeviance_two_streams(data1,data2,t,k,u):
    '''Return the codeviance between two streams'''
    
    
    
    repartition1 = partition(data1,m,t,u)
    repartition2 = partition(data2,m,t,u)
    
    cod_vect = np.array([0. for i in range(k)], dtype = float)
    
    for i in range(t):
        cod = codeviance(repartition1[i], repartition2[i])
        cod_vect[i] = cod
    
    return min_vect(cod_vect)
    
    
def codeviance_all_streams(DATA,eps,delta,u):
    ''' DATA = array of steams
    Return the codevianc matrix'''
    n = len(DATA)
    cod_matrix = np.array([[0. for i in range(n)] for j in range(n)], dtype = float)
    
    m = np.ceil( np.ln( 1 / delta ) )
    k = 1 / eps
    
    for i in range(n):
        for j in range(i,n):
            cod = codeviance_two_streams(DATA[i], DATA[j], m, k, u)
            cod_matrix[i,j] = cod
            cod_matrix[j,i] = cod
    
    return cod_matrix
