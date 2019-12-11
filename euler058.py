'''Euler 58 Spiral Primes
March 1, 2018'''

from math import sqrt

diagnums = [1]

def diags(n):
    '''returns diagonal numbers for
    square spiral with sidelength n'''
    
    global diagnums
    primes = 0
    tr = (n-2)**2 + (n-1)
    for i in range(4):
        new = tr + i*(n-1)
        diagnums.append(new)
        if isPrime(new):
            primes += 1
    #print(n,primes)
    return primes

def isPrime(n):
    for i in range(3,int(sqrt(n))+1,2):
        if n % i == 0:
            return False
    return True

def percentPrimes(mylist):
    primes = 0
    for thing in mylist:
        if isPrime(thing):
            primes += 1
    return primes / len(mylist)

i = 3
primes = 0
while True:
    
    primes += diags(i) #add to the list
    p = primes / len(diagnums)
    #print(primes,diagnums)
    if i % 1001 == 0: print(i,p)
    if p < 0.1:
        print(i,p)
        break
    i += 2

'''
output:
1001 0.14992503748125938
3003 0.13322231473771856
5005 0.12508742132081127
7007 0.11881824020552344
9009 0.11350391297108287
11011 0.11166613686935198
13013 0.10851104707012488
15015 0.10629724599553765
17017 0.10539770223018835
19019 0.10381996477114389
21021 0.10256654218500987
23023 0.1018785970246498
25025 0.1008012148094867
26241 0.09999809454850327 #so the answer: 26241
'''
