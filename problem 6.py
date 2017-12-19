def sumofsquares(x):
    a = 0
    for i in range(x+1):
        a += i ** 2
    return a

def squareofsums(x):
    a = 0
    for i in range(x+1):
        a += i
    return a ** 2

print squareofsums(100) - sumofsquares(100)
