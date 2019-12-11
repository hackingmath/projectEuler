'''Euler 66 Diophantine equation
Mar. 1, 2018'''

from math import sqrt

#x**2 - D*y**2 = 1

def x(D,y):
    x = sqrt(D*y**2 + 1)
    if x == int(x):
        return x
    return 0

def gcf(a,b):
    for i in range(min(a,b),0,-1):
        if a % i == 0 and b % i == 0:
            return i

def maxX():
    '''Finds the maximum value of x
    for range of D and y'''
    exxes = dict()
    for D in range(1,10001):
        for y in range(1001,100001):
            x1 = x(D,y)
            if gcf(D,y) == 1:
                exxes[x1] = [D,y]
    max_x = max(exxes)
    return max_x,exxes[max_x]
            

print(maxX())
