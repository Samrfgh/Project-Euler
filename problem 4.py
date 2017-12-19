def largestpallindrome(a,b):
    i = 0
    for x in range(b, a, 1):
        for y in range(b, a, 1):
            z = x * y
            if str(z) == str(z)[::-1]:
                if i < z:
                    i = z
    return i

print largestpallindrome(999,100)
