import math
def is_prime(x,plist):
    if x == 1:
        return False
    for i in plist:
        if x % i == 0:
            return False
    return True

def list_of_primes(begin,end):
    plist = []
    for i in range(2,end):
        if is_prime(i,plist):
            plist.append(i)
    return [x for x in plist if x > 1000]


z = list_of_primes(1000,10000)
z_set = set(z)
for a_i,a in enumerate(z):
    for b in z[a_i + 1:]:
        c = b + (b - a)
        if c in z_set and set(str(a)) == set(str(b)) == set(str(c)):
            print([a,b,c])
