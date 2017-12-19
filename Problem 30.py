def digits_fifth_powers(x):
    y = 0
    for i in str(x):
        y += int(i) ** 5
    if y == x:
        return True

list1 = []
for i in range(2,355000):
    if digits_fifth_powers(i) == True:
        list1.append(i)
print sum(list1)
