def dec_to_bin(x):
    return int(bin(x)[2:])

def base_10_pallindrome(x):
    if str(x) == str(x)[::-1]:
        return True

def base_2_pallindrome(x):
    if str(dec_to_bin(x)) == str(dec_to_bin(x))[::-1]:
        return True

def double_base_pallindrome(x):
    a = 0
    for i in range(1,x):
        if base_10_pallindrome(i) and base_2_pallindrome(i):
            a += i
    return a

print(double_base_pallindrome(1000000))
