import math

def triangle_list(x):
    tlist = []
    for i in range(1,x + 1):
        tlist.append(i * (i + 1) / 2)
    return tlist

def num_to_tri(x):
    return x * (x + 1) / 2

def is_pentagonal(x):
    y = (math.sqrt(24 * x + 1) + 1) / 6
    if y == int(y):
        return True

def is_hexagonal(x):
    y = (math.sqrt(8 * x + 1) + 1) / 4
    if y == int(y):
        return True

def find_d(list1):
    d = []
    while len(d) < 1:
        x = num_to_tri(len(list1) + 1)
        if is_pentagonal(x) and is_hexagonal(x):
            d.append(x)
        else:
            list1.append(x)
    return d

print(find_d(triangle_list(285)))
