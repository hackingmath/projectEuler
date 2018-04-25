'''Project Euler Problem 102
Triangle Containment
April 24, 2018
Using urllib to work with online text file'''

from urllib.request import urlopen

points = []

url = "https://projecteuler.net/project/resources/p102_triangles.txt"

data = urlopen(url).readlines()
for i,line in enumerate(data):
    
    line = line.decode('utf-8').strip().split(',')
    points.append([])
    for num in line:
        points[i].append(int(num))


def line2pts(p1,p2):
    #line between two points
    if p2[0]-p1[0] == 0:
        m = p2[0]
    else:
        m = (p2[1]-p1[1])/(p2[0]-p1[0]) #slope
    b = p1[1] - m*p1[0]
    return m,b

def inequalities(myList):
    '''Returns True if the origin is on the same
    side of each side of the triangle as the opposite
    point'''
    #first put the numbers into x-y points
    pt1 = (myList[0],myList[1])
    pt2 = (myList[2],myList[3])
    pt3 = (myList[4],myList[5])
    #the lines (sides) formed by joining points
    lines = [line2pts(pt1,pt2),
             line2pts(pt2,pt3),
             line2pts(pt3,pt1)]
    #put points in order of opposite sides, for
    #example pt3 is opposite the line formed by
    #pt1 and pt2
    points = [pt3,pt1,pt2]
    #create a list to store inequalities
    output = []
    #go through the lines and points
    for i,line in enumerate(lines):
        #if opposite point is under the line
        if points[i][1] < line[0]*points[i][0] + line[1]:
            output.append('less')
        else:
            output.append('greater')
    origin = [] #store inequalities for the origin
    for line in lines:
        if 0 < line[1]: #is the origin under the line
            origin.append('less')
        else: #Or over the line:
            origin.append('greater')
    #compare the inequalities. If the origin matches the
    #opposite points, it's within the triangle.
    return output == origin
         

origins = 0
count = 0
for thing in points:
    count += 1
    if inequalities(thing):
        origins += 1

print("origins:",origins,"count:",count)

#correct!
