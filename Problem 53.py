def factorial(x):
    y = 1
    for i in range(1,x + 1):
        y *= i
    return y

def combinatoric_selections(x):
    clist = []
    for n in range(23,101):
        for r in range(1,n):
            if factorial(n) / (factorial(r) * factorial(n - r)) > x:
                clist.append([n,r])
    return clist

print(len(combinatoric_selections(1000000)))
