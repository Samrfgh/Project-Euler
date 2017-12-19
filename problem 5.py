def divisible(x):
    for i in range(11,21):
        if x % i == 0:
            continue
        else:
            return False
    return True

x = 2520
while not divisible(x):
    x += 2520
print (x)
