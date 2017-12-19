def nextfibs(list1):
    l = len(list1)
    return list1[l-1] + list1[l-2]

def newfibnumber():
    fibs = [1,1]
    while nextfibs(fibs) <= 4000000:
        fibs.append(nextfibs(fibs))
    return fibs

def evensum(list1):
    total = 0
    for x in list1:
        if x % 2 == 0:
            total = total + x
    return total

print evensum(newfibnumber())
