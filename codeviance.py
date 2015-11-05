import numpy as np

def average(X):
    """Return the average of X"""
    
    n = 0
    S = 0
    for e in X:
        S = S + e
        n += 1
    return S / n


def codeviance(X, Y):
    """Return the codeviance of X annd Y"""
    
    av_x = average(X)
    av_y = average(Y)
    return average(X*Y) - (av_x * av_y)


def average_sketchmin(X):
    n = 0
    S = 0
    for i in range(len(X)):
        S = S + X[i]*i
        n += X[i]
    return S / n
