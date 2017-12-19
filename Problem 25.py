def nextfibs(list1):
    l = len(list1)
    return list1[l-1] + list1[l-2]

def newfibnumber(x):
    fibs = [1,1]
    curret_fib = 2
    while len(str(curret_fib)) < x:
        fibs.append(curret_fib)
        curret_fib = nextfibs(fibs)
    return fibs

print(len(newfibnumber(1000)) + 1)
