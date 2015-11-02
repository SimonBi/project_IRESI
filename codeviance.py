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
    
    
def mult_sketch_vect(X, Y):
    X2 = np.copy(X)
    Y2 = np.copy(Y)
    Z = np.array([0. for i in range(len(X)*len(Y))])
    i,j = 0, 0
    while i < len(X) and j < len(Y):
        if X2[i] == Y2[j]:
            Z[i*j] += X2[i]
            i += 1
            j += 1
        elif X2[i] > Y2[j]:
            Z[i*j] += Y2[j]
            X2[i] -= Y2[j]
            j += 1
        else:
            Z[i*j] += X2[i]
            Y2[j] -= X2[i]
            i += 1
    return Z
    
    
def codeviance_sketchmin(X,Y):
    av_x = average_sketchmin(X)
    av_y = average_sketchmin(Y)
    Z = mult_sketch_vect(X, Y)
    return average_sketchmin(Z) - (av_x * av_y)
        
#X = np.array([2, 5, 3]) # 0 0 1 1 1 1 1 2 2 2
#Y = np.array([1, 4, 5]) # 0 1 1 1 1 2 2 2 2 2
                        ## 0 0 1 1 1 2 2 4 4 4
#Z = mult_sketch_vect(X, Y)

#print(Z)
