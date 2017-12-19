import math

def triangular(x):
    a = 1
    while type(a) == int:
        t = a * (1 + a) / 2
        if len(factors(t)) >= x:
            return t
        else:
            a += 1

def factors(x):
    flist = []
    for i in range(1,int(math.sqrt(x)) + 1):
        if x % i == 0:
            flist.append(i)
            flist.append(x / i)
    return flist

print(triangular(500))
