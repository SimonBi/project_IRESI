from math import sqrt


def average(list_x):
    """Return the average of list_x"""
    
    n = 0
    s = 0
    for e in list_x:
        s = s + e
        n += 1
    return s / n


def codeviance(list_x, list_y):
    """Return the codeviance of list_x and list_y"""
    
    av_x = average(list_x)
    av_y = average(list_y)
    return abs(average(list_x*list_y) - (av_x * av_y))


def stdev(list_x):
    """ Return tje standard deviation of list_x"""
    return sqrt(codeviance(list_x, list_x))
