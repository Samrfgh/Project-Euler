dict1 = {0:1}
def factorial(x):
    if x in dict1:
        return dict1[x]
    product = 1
    y = x
    while x != 1:
        product *= x
        x = x - 1
    dict1[y] = product
    return product

def digit_factorial(x):
    result = 0
    for i in str(x):
        result += factorial(int(i))
    if result == x:
        return True

def sum_of_factorials(upper_bond):
    result = 0
    for i in range(3,upper_bond):
        if digit_factorial(i) == True:
            result += i
    return result

print(sum_of_factorials(2540160))
