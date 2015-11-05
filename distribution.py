from numpy.random import *


def entry_uniform(size, u):
    """ return a random entry with values in
    {0..u} following distribution """
    entries = []
    for i in range(size):
        x = int(uniform(0,u))
        entries.append(x)
    return entries


def entry_zipfian(size, u, alpha):
    """ return a random entry with values in
    {0..u} following distribution """
    entries = []
    for i in range(size):
        x = zipf(alpha)
        while x > u or x < 0:
            x = zipf(alpha)
        entries.append(x)
    return entries
    

def entry_poisson(size, u, lambd):
    """ return a random entry with values in
    {0..u} following distribution """
    entries = []
    for i in range(size):
        x = poisson(lambd)
        while x > u or x < 0:
            x = poisson(lambd)
        entries.append(x)
    return entries
    
def entry_binomial(size, u, p):
    """ return a random entry with values in
    {0..u} following distribution """
    entries = []
    for i in range(size):
        x = binomial(u,p)
        entries.append(x)
    return entries
    
def entry_negative_binomial(size, u, p):
    """ return a random entry with values in
    {0..u} following distribution """
    entries = []
    for i in range(size):
        x = negative_binomial(u,p)
        while x > u or x < 0:
            x = negative_binomial(u,p)
        entries.append(x)
    return entries
