'''Project Euler problem 23'''

from time import time

t1 = time()

def factors(num):
  return [n for n in range(1,int(num/2)+1) if num % n == 0]
  
def abundant(num):
  return sum(factors(num)) > num
  
nums = [x for x in range(1,28124)]

print("nums are done.")
  
abundantList = [n for n in range(1,28124) if abundant(n)]

print("abundants are done.")

for a in abundantList:
    for b in abundantList:
        if b >= a:
            thesum = a + b
            if thesum > 28123:
                continue
            if thesum in nums:
                nums.remove(thesum)
      
print(sum(nums))

print(time() - t1)
