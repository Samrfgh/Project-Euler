import math
def is_prime(x):
    if x == 1:
        return False
    for i in range(2,int(math.sqrt(x)) +1):
        if x % i == 0:
            return False
    return True

def pandigital_list(x):
    plist = []
    for i in range(2,x):
        if is_pandigital(i) and is_prime(i):
            plist.append(i)
    return plist

def is_pandigital(x):
    for i in range(1,len(str(x)) + 1):
        if str(x).count(str(i)) == 1:
            continue
        else:
            return False
    return True


print(max(pandigital_list(9876543)))
