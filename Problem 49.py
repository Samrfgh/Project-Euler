import math
def new_is_prime(x,plist):
    if x == 1:
        return False
    for i in plist:
        if i > int(math.sqrt(x)):
            return True
        if x % i == 0:
            return False
    return True

def is_prime(x):
    if x == 1:
        return False
    for i in range(2,int(math.sqrt(x)) +1):
        if x % i == 0:
            return False
    return True

def list_of_primes(x):
    plist = []
    for i in range(2,x):
        if is_prime(i):
            plist.append(i)
    return plist

def perm_prime(x,y,z,plist):
    if y > 9999 or z > 9999:
        return False
    if set(str(x)) == set(str(y)) == set(str(z)):
        if new_is_prime(x,plist) and new_is_prime(y,plist) and new_is_prime(z,plist):
            return True
    return False

z = list_of_primes(100)
plist = []
x = 1000
while len(plist) < 2:
    if new_is_prime(x,z):
        for i in range(1000,3334,2):
            if perm_prime(x,x + i,x + i + i,z):
                plist.append([x,x + i,x + i + i])
    x += 1
print(plist)
