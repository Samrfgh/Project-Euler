def factorial(x):
    current = 1
    for i in range(1,x+1):
        current = i * current
    return current

def sumofdigits(x):
    current = 0
    for i in str(x):
        current += int(i)
    return current

print sumofdigits(factorial(100))
