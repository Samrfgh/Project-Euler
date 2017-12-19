def pandigital_list(x):
    plist = []
    for i in range(1023456788,x):
        if is_pandigital(i):
            plist.append(i)
    return plist

def is_pandigital(x):
    for i in range(1,len(str(x)) + 1):
        if str(x).count(str(i)) == 1:
            continue
        else:
            return False
    return True

print(pandigital_list(9876543211))
