def self_powers(x):
    n = 0
    for i in range(1,x + 1):
        n += i ** i
    return n

print(str(self_powers(1000))[-10:])
