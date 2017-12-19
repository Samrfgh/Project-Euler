import math
def is_pentagonal(x):
    y = (math.sqrt(24 * x + 1) + 1) / 6
    if y == int(y):
        return True

def num_to_pent(x):
    return ((3 * x - 1) * x) / 2

def sum_and_difference(x,y):
    if is_pentagonal(x + y) and is_pentagonal(y - x):
        return True

def find_d(list1):
    d = 0
    while d == 0:
        x = num_to_pent(len(list1) + 1)
        for i in list1:
            if sum_and_difference(i,x):
                d = x - i
                return d
        list1.append(x)

print(find_d([1]))
