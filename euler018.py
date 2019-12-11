'''Euler 18 and 67'''

with open("triangle2.txt")as f:
    lst = []
    for line in f.readlines():
        lst.append([int(x) for x in line.split()])


for r in range(len(lst)-2,-1,-1):
    for c in range(len(lst[r])):
        max1 = max(lst[r+1][c],lst[r+1][c+1])
        lst[r][c] += max1
        #print(lst[r][c],end=', ')
    #print()
print(lst[0][0])


'''
50 
12 65 
86 93 32 
69 67 17 56 
91 39 01 35 42
Solution: 314

triangle2.txt
Solution: 14628
'''
