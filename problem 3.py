import math
def is_prime(x):
    if x == 1:
        return False
    for i in range(2,int(math.sqrt(x)) +1):
        if x % i == 0:
            return False
    return True

def factors(x):
    flist = []
    for i in range(1,int(math.sqrt(x)) +1):
        if x % i == 0:
            flist.append(i)
            flist.append(x / i)
    return prime_factors(flist)

def prime_factors(list1):
    plist = []
    for i in list1:
        if is_prime(i):
            plist.append(i)
    return plist

print(factors(36))
