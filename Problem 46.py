import math
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

def composite_square_num(x):
    for i in list_of_primes(x):
        y = (x - i) / 2
        if int(math.sqrt(y)) == math.sqrt(y):
            return True
    return False

d = 0
x = 9
while d == 0:
    if is_prime(x) != True:
        if composite_square_num(x):
            x += 2
        else:
            d += x
    else:
        x += 2
print(d)
