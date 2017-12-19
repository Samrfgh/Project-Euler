import math

def sum_of_divisors(x):
    list1 = [1]
    for i in range(2,int(math.sqrt(x)) + 1):
        if x % i == 0:
            list1.append(i)
            list1.append(x / i)
    return sum(list1)

def amicable_numbers(x):
    list1 = []
    for i in range(2,x):
        if i == sum_of_divisors(sum_of_divisors(i)):
            if i != sum_of_divisors(i):
                list1.append(i)
    return (list1)

print(sum(amicable_numbers(10000)))
