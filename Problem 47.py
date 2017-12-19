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

def consecutive_num(n):
    flist = []
    x = 210
    while len(flist) == 0:
        if len(factors(x)) == n and len(factors(x + 1)) == n and len(factors(x + 2)) == n and len(factors(x + 3)) == n:
            flist.append(x)
            flist.append(x + 1)
            flist.append(x + 2)
            flist.append(x + 3)
        x += 1
    return flist

print(consecutive_num(4))
