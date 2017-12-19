import math
def is_prime(x):
    if x == 1:
        return False
    for i in range(2,int(math.sqrt(x)) +1):
        if x % i == 0:
            return False
    return True

def list_of_primes(x):
    plist = [2]
    for i in range(3,x,2):
        if new_is_prime(i,plist):
            plist.append(i)
    return plist

def new_is_prime(x,plist):
    if x == 1:
        return False
    for i in plist:
        if i > int(math.sqrt(x)):
            return True
        if x % i == 0:
            return False
    return True

def consecutive_sum_primes(x):
    y = list_of_primes(x)
    s = set(y)
    largest = [0,0]
    for a in range(len(y)):
        if a * largest[1] > x:
            return largest
        for b in range(a + largest[1],len(y)):
            j = y[a:b + 1]
            w = sum(j)
            if w > x:
                break
            if w in s and largest[1] < len(j):
                largest = [w,len(j)]
    return largest

print(consecutive_sum_primes(1000000))
