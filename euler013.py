"""Finding first 10 digits of sum of 100 50-digit numbers
August 17, 2019"""

with open("fiftydigitnumbers.txt") as f:
    #data = f.read().split() #don't need to 'read' and 'split'?
    nums = [int(n) for n in f]

s = sum(nums)
stra = str(s)
print(stra[:10])
