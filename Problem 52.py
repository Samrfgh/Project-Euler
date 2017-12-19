y = 0
x = 10
while y == 0:
    if set(str(1 * x)) == set(str(2 * x)) == set(str(3 * x)) == set(str(4 * x)) == set(str(5 * x)) == set(str(6 * x)):
        y = x
    else:
        x += 1
print(y)
