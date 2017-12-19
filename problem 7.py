import math
def isprime(x):
    for i in range(2,int(math.sqrt(x)) +1):
        if x % i != 0:
            continue
        else:
            return False
    return True

def nthprime(x):
    plist = []
    a = 2
    while len(plist) < x:
        if isprime(a):
            plist.append(a)
            if len(plist) == x:
                return max(plist)
        a += 1

print(isprime(307))
