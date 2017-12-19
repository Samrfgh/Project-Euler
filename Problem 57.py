from fractions import Fraction

def a(d):
    f = [0,1]
    for i in range(d,1,-1):
        [x,y] = f
        f = [y, 2 * y + x]
    return f

def root_two(d):
    [x, y] = [int(a(d)[0]) + int(a(d)[1]), a(d)[1]]
    return [x, y]

def square_root_convergent(x):
    count = 0
    for i in range(1,x + 1):
        if len(str(root_two(i)[0]))> len(str(root_two(i)[1])):
            count += 1
    return count

print(square_root_convergent(1000))
