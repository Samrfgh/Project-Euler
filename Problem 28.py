def sum_of_spiral(side_length):
    spiral = []
    i = side_length ** 2
    if side_length == 1:
        return 1
    while len(spiral) < 4:
        spiral.append(i)
        i = i - side_length + 1
    return sum(spiral)

x = 0
for i in range(1,1002,2):
    x += sum_of_spiral(i)
print(x)
