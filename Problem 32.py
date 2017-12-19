import math

digits = set([1,2,3,4,5,6,7,8,9])

def factors(x):
    factor_list = []
    for i in range(1,int(math.sqrt(x)) + 1):
        if x % i == 0:
            factor_list.append(i)
            factor_list.append(x / i)
    return factor_list

def pandigital(list1):
    for i in range(0,len(list1) - 1,2):
        pandigital_list = []
        for a in str(list1[i]):
            pandigital_list.append(int(a))
        for b in str(list1[i + 1]):
            pandigital_list.append(int(b))
        for c in str(list1[i] * list1[i + 1]):
            pandigital_list.append(int(c))
        if len(pandigital_list) == 9 and set(pandigital_list) == digits:
            return (list1[i] * list1[i + 1])
        else:
            continue

plist = []
x = 0
while x < 99999:
    if len(str(x)) == len(set(str(x))) and type(pandigital(factors(x))) == int:
        plist.append(x)
    x += 1
print(sum(plist))
