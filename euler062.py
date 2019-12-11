'''Euler 062 Cubic Permutations
Mar. 1, 2018'''

cubes = []
cube_twins = dict()

for i in range(100,10000):
    cubes.append(str(i**3))
print("cubes done.")

for strnum in cubes:
    cube_twins[strnum] = []
    for othernum in cubes:
        if len(strnum) == len(othernum):
            if sorted(strnum) == sorted(othernum):
                #print(strnum,othernum)
                cube_twins[strnum].append(int(othernum))

    if len(cube_twins[strnum]) >= 5:
        print(strnum,cube_twins[strnum])
        
        print(sum(cube_twins[strnum]))

    
    
