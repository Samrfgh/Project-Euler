def multiples(i):
    sum_of_multiples = 0
    for x in range(1,i):
        if x % 3 == 0 or x % 5 == 0:
            sum_of_multiples += x
    return sum_of_multiples

print(multiples(1000))
