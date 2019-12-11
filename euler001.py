'''Project Euler problem 1
Multiples of 3 or 5
June 8, 2018'''

import time
time1 = time.time()

def main():
    mults = set()
    n = 1
    while 3*n < 1000:
        mults.add(3*n)
        if 5*n < 1000:
            mults.add(5*n)
        n+=1

    print(sum(mults))

#main()

def main2():
    mults = set()
    for n in range(1,1000):
        if n % 3 == 0 or n % 5 == 0:
            mults.add(n)
    print(sum(mults))

main2()

print(time.time() - time1)
