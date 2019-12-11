'''Euler Problem #75
Singular Integer Right Triangles
March 8, 2018'''

from math import sqrt

maximum = 1500000

def irt(L):
    '''Returns the number of Integer
    Right Triangles with Perimeter L'''
    irts = 0
    for side1 in range(1,L//2+1):
        for side2 in range(1,side1 + 1):
            if L - side1 - side2 != (side1**2 + side2**2)**(0.5):
                 continue
##            if side2 == side1:
##                irts += 0.5
            else:
                irts += 1
    
    return irts

irts = {i:0 for i in range(1,maximum)}

for side1 in range(1,maximum//2 + 1):
    for side2 in range(1,side1 + 1):
        side3 = sqrt(side1**2 + side2**2)
        if side3 == int(side3):
            #print(side1,side2,side3)
            perim = int(side1 + side2 + side3)
            try:
                irts[perim] += 1
            except KeyError:
                pass

count = 0
for i in irts:
    if i % 10000 == 0:
        print(i,count)
    if irts[i] == 1:
        print(i)
        count += 1

##sirts = 0
##for L in range(3,1500001):
##    if L % 100 == 0:
##        print(L,sirts)
##    if irt(L) == 1.0:
##        sirts += 1

print(count)
