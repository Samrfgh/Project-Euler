def list_of_recurring(lst,min_len):
    l = len(lst)
    for i in range(l):
        if (l - i) % 2 != 0:
            continue
        first_half = lst[i:(l - i) / 2 + i]
        second_half = lst[(l - i) / 2 + i:]
        if first_half == second_half and len(first_half) >= min_len:
            return first_half
    return []

def len_of_recurring(x):
    lst = []
    a = 1
    while list_of_recurring(lst,len(str(x))) == []:
        lst.append((a * 10)/x)
        a = (a * 10) % x
    return len(list_of_recurring(lst,len(str(x))))

def below_x(x):
    current = 0
    largest = 0
    d = 0
    for i in range(1,x):
        current = len_of_recurring(i)
        if current > largest:
            largest = current
            d = i
    return d

#print(below_x(1000))
print len_of_recurring(593)
