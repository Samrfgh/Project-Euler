def is_pallindrome(x):
    if str(x) == str(x)[::-1]:
        return True
    else:
        return False

def is_lycherl(x):
    nlist = []
    while len(nlist) < 50:
        nlist.append(1)
        if is_pallindrome(x + int(str(x)[::-1])):
            return False
        else:
            x = x + int(str(x)[::-1])
    return True

def lycherl_numbers(x):
    llist = []
    for i in range(1,x):
        if is_lycherl(i):
            llist.append(i)
    return llist

print(len(lycherl_numbers(10000)))
