def digit_sum(x):
    y = 0
    for i in str(x):
        y += int(i)
    return y

largest = 0
for a in range(1,100):
    for b in range(1,100):
        d = digit_sum(a ** b)
        if d > largest:
            largest = d
print(largest)
