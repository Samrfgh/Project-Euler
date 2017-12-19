def longestcollatz(x):
    longest = []
    for i in range(1,x):
        y = collatz(i)
        if len(y) > len(longest):
            longest = y
    return longest[0]

def collatz(x):
    list1 = [x]
    while True:
        if x % 2 == 0:
            x = x / 2
            list1.append(x)
        else:
            if x == 1:
                return list1
            else:
                x = 3 * x + 1
                list1.append(x)



print longestcollatz(1000000)
