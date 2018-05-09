'''Euler 102
May 8, 2018
with Aryan'''

from math import sqrt

file = "/home/peter/p102_triangles.txt"

with open(file) as f:
    nums = []
    points = []
    for line in f.readlines():
        data = line.split(',')
        #tris.append(data.strip())
        for p in data:
            nums.append(int(p))
    #print(tris[:10])
    #groups points by 6
    for x in range(0,len(nums),6):
        points.append(nums[x:x+6])

#myList = [-340,495,-153,-910,835,-947]


def line2pts(p1,p2):
    if p2[0] - p1[0] ==0: #vertical line
        m = 1000000 #close to infinite slope
    else:
        m = (p2[1]-p1[1])/(p2[0]-p1[0]) #slope
    b = p1[1] - m*p1[0]
    return m,b

def sideLength(p1,p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def heron(a,b,c):
    '''returns the area of a triangle
    with 3 given sidelengths'''
    s = (a + b+ c)/2.0
    return sqrt(s*(s-a)*(s-b)*(s-c))

def area(myList):
    p1 = (myList[0],myList[1])
    p2 = (myList[2],myList[3])
    p3 = (myList[4],myList[5])
    a,b,c = sideLength(p1,p2),sideLength(p2,p3),sideLength(p1,p3)
    return heron(a,b,c)

def areaOrigin(myList):
    '''returns True if the sum of the areas of the triangles
    equals the area of the big triangle'''
    p1 = (myList[0],myList[1])
    p2 = (myList[2],myList[3])
    p3 = (myList[4],myList[5])
    origin = (0,0)
    #triangle1 - big one
    a,b,c = sideLength(p1,p2),sideLength(p2,p3),sideLength(p1,p3)
    a1 = heron(a,b,c)
    #triangle2
    a,b,c = sideLength(p1,p2),sideLength(p2,origin),sideLength(p1,origin)
    a2 = heron(a,b,c)
    #triangle3
    a,b,c = sideLength(p1,origin),sideLength(origin,p3),sideLength(p1,p3)
    a3 = heron(a,b,c)
    #triangle4
    a,b,c = sideLength(origin,p2),sideLength(p2,p3),sideLength(origin,p3)
    a4 = heron(a,b,c)
##    print(a1)
##    print(a2+a3+a4)
    return round(a1,3) == round(a2 + a3 + a4,3)

#print(areaOrigin(myList))

origins = 0
count = 0
for thing in points:
    count += 1
    if areaOrigin(thing):
        origins += 1

print("origins:",origins,"count:",count)
