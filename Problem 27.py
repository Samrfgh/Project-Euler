import math
def is_prime(x):
    for i in range(2,int(math.sqrt(x)) +1):
        if x % i != 0:
            continue
        else:
            return False
    return True

def quadratic_primes(a,b):
    list1 = []
    i = 0
    while True:
        if (i ** 2 + a * i + b) < 0:
            return list1
        elif is_prime(i ** 2 + a * i + b) == True:
            list1.append(i ** 2 + a * i + b)
            i += 1
        else:
            return list1
    return list1

def maximum_number_of_primes():
    largest = []
    coefficients = []
    for i in range(-999,1000):
        for j in range(-1000,1000):
            x = quadratic_primes(i,j)
            if len(largest) < len(x):
                largest = x
                coefficients = [i,j]
    return coefficients

print(maximum_number_of_primes())
