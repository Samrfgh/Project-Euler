def sumofdigits(x):
    list1 =[]
    for i in str(2 ** x):
        list1.append(int(i))
    return sum(list1)


print sumofdigits(1000)
