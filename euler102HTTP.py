'''Project Euler Problem 102
Triangle Containment
April 24, 2018
Using urllib to work with online text file'''

from urllib.request import urlopen

points = []

url = "https://projecteuler.net/project/resources/p102_triangles.txt"

data = urlopen(url).readlines()#.decode('utf-8')#.split('\n')
for i,line in enumerate(data):
    
    line = line.decode('utf-8').strip().split(',')
    points.append([])
    for num in line:
        #num = int(num)
        #print(num,type(num))
        points[i].append(int(num))

myList = [-340, 495, -153, -910, 835, -947]

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
         

def intersection(line1,line2):
    '''returns the intersection of
    y = ax + b and y = cx + d'''
    a,b,c,d = line1[0],line1[1],line2[0],line2[1]
    x = (d - b) / (a - c)
    y = a*x + b
    return (x,y)

def lineSlopePt(m,pt):
    b = pt[1] - m*pt[0]
    return m,b

def perpBisector(pt1,pt2):
    slope2pts = (pt2[1]-pt1[1])/(pt2[0]-pt1[0])
    mdpt = [(pt2[0] + pt1[0])/2.0,
            (pt2[1] + pt1[1])/2.0]
    m = -1.0/slope2pts
    return lineSlopePt(m,mdpt)

def centroid(pt1,pt2,pt3):
    pb1 = perpBisector(pt1,pt2)
    pb2 = perpBisector(pt2,pt3)
    return intersection(pb1,pb2)


def hasOrigin(ptsList):
    pt1 = [ptsList[0],ptsList[1]]
    pt2 = [ptsList[2],ptsList[3]]
    pt3 = [ptsList[4],ptsList[5]]
    
#print(centroid((-340, 495), (-153, -910), (835, -947)))

#print(inequalities([-175,41,-421,-714,574,-645]))

origins = 0
count = 0
for thing in points:
    count += 1
    if inequalities(thing):
        origins += 1

print("origins:",origins,"count:",count)

#correct! 228 out of 1000
