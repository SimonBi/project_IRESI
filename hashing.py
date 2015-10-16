import numpy as np
from random import randint


# Entry : a pile of integers bewteen 0 and u-1

# We create k partitions
# We use m different hashing functions

def hashing(a,b,x,u,k):
    '''Universal hashing function'''
    y = ((a*x + b) % u) % k
    return y
    

def choosehashfunctions(t):
    '''Create m different hasing functions by randomly
    choosing values for a and b'''
    hash_f = np.array([[0.,0.] for i in range(t)])
    for i in range(m):
        a = randint(1, m-1)
        b = randint(0, m-1)
        hash_f[i,0], hash_f[i,1] = a,b
    return hash_f


def partition(data,t,k,u):
    '''Return a m*x matrix once hashing 
    functions have been applied to data'''
    
    hash_f = choosehashfunctions(t)
    
    repartition = np.array([[0. for j in range(k)] for i in range(t)], dtype = float)
    
    while data != []:
        x = data.pop()
        for i in range(m):
            j = hashing(hash_f[i,0], hash_f[i,1], x, u, k)
            repartition[i,j] += 1
    
    return repartition
    
    
    
