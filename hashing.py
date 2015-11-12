import numpy as np
from random import randint


# Entry : a pile of integers between 0 and u-1

# We create k partitions
# We use m different hashing functions

def hashing(a, b, x, u, k):
    """
    Universal hashing function
    """
    return ((a * x + b) % u) % k


def choosehashfunctions(t):
    """
    Create t different hashing functions by randomly
    choosing values for a and b.
    :param t: Number of hashing functions.
    """
    hash_f = np.array([[0, 0] for _ in range(t)])
    for i in range(t):
        a = randint(1, t-1)
        b = randint(0, t-1)
        hash_f[i, 0], hash_f[i, 1] = a, b

    return hash_f


def partition(data, t, k, u, hash_f):
    """
    Return a t*x matrix once hashing
    functions have been applied to data
    :param hash_f: Hashing function.
    """
    
    repartition = np.array([[0 for _ in range(k)] for _ in range(t)])
    data_copy = data[:]
    while data_copy != []:
        x = data_copy.pop()
        for i in range(t):
            j = hashing(hash_f[i, 0], hash_f[i, 1], x, u, k)
            repartition[i, j] += 1
    
    return repartition
