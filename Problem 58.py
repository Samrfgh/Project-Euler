import math
def is_prime(x):
    if x == 1:
        return False
    for i in range(2,int(math.sqrt(x)) +1):
        if x % i != 0:
            continue
        else:
            return False
    return True

def spiral_numbers(x):
    plist = [3,5,7]
    slist = [1,3,5,7,9]
    a = 9
    i = 4
    while percentage(plist,slist) > x:
        a += i
        if is_prime(a):
            plist.append(a)
        slist.append(a)
        a += i
        if is_prime(a):
            plist.append(a)
        slist.append(a)
        a += i
        if is_prime(a):
            plist.append(a)
        slist.append(a)
        a += i
        if is_prime(a):
            plist.append(a)
        slist.append(a)
        i += 2
    return int(math.sqrt(a))

def percentage(lst1,lst2):
    x = len(lst1)
    y = len(lst2)
    return float(x)/float(y)


print(spiral_numbers(0.1))
