import math
def truncatable_primes(x):
    plist = []
    i = 11
    while len(plist) < x:
        if ltr(i, True) and ltr(i, False):
            plist.append(i)
        i += 2
    return plist

def ltr(x, is_from_left):
    y = str(x)
    if is_prime(x):
        while len(y) > 1:
            if is_from_left:
                y = y[1:]
            else:
                y = y[:-1]
            if is_prime(int(y)):
                continue
            else:
                return False
    else:
        return False
    return True


def is_prime(x):
    if x == 1:
        return False
    for i in range(2,int(math.sqrt(x)) +1):
        if x % i == 0:
            return False
    return True

print(sum(truncatable_primes(11)))
