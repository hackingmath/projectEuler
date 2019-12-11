'''Euler 120 Square Remainders'''

def R(a,e):
    '''Finds largest remainder when
    (a-1)**n + (a+1)**n is divided by
    a**e
    '''
    n = 0
    record = 0
    while n < 1000:
        
        rem = ((a-1)**n + (a+1)**n) % (a**e)
        if rem > record:
            record = rem
        n += 1
    print("R(",a,",",e,")=",record)
    return record


def sumR(A,e):
    '''Sum of all lgst remainders
    Answer is mod 10**9 + 7'''
    total = 0
    a = 1
    while a <= A:
        total += R(a,e) #e can be 2 or 3
        total %= (10**9 + 7)
        a += 1
    return total

print(sumR(2,2))
