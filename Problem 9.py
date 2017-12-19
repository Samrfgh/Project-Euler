def specialtriplet(x):
    for a in range(1,x):
        for b in range(a,x):
            c = x - a - b
            if a**2 + b**2 == c**2:
                return a*b*c

print specialtriplet(1000)
