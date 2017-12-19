import math
def is_prime(x):
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

def circular_prime(x):
    circular_plist = [x]
    a = list(str(circular_plist[-1]))
    while len(circular_plist) < len(str(x)):
        a.append(a[0])
        a.remove(a[0])
        if is_prime(int(''.join(a))):
            circular_plist.append(int(''.join(a)))
            continue
        else:
            return False
    return True

x = []
for i in list_of_primes(1000000):
    if circular_prime(i):
        x.append(i)
print(len(x))
