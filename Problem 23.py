import math

def abundant_numbers(x):
    abundant_list = []
    for i in range(1,x):
        if is_abundant(i):
            abundant_list.append(i)
    return abundant_list


def divisors(x):
    flist = [1]
    for i in range(2,int(math.sqrt(x)) + 1):
        if x % i == 0:
            flist.append(i)
            if x / i != i:
                flist.append(x / i)
    return flist

def is_abundant(x):
    return sum(divisors(x)) > x


def is_sum_of_abundant(x,numbers,a_set):
    for a in numbers:
        if a >= x:
            return False
        else:
            if x - a in a_set:
                return True
    return False


def sum_of_numbers(x):
    y = 0
    a = abundant_numbers(x)
    a_set = set(a)
    for i in range(1,x):
        if not is_sum_of_abundant(i,a,a_set):
            y += i
    return y

print(sum_of_numbers(28123))
