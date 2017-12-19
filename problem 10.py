import math

def primes(x):
    plist = [2]
    for i in range(3,x,2):
        if isprime(plist,i) == True:
            plist.append(i)
    return plist

def isprime(plist,x):
    for i in plist:
        if i**2 > x:
            return True
        if x % i == 0:
            return False
    return True

print sum(primes(2000000))
