import math
def right_triangles(x):
    solutions = []
    for a in range(2,int(x / 3) + 1):
        for b in range(a,x):
            c = int(math.sqrt(a ** 2 + b ** 2))
            if a ** 2 + b ** 2 == c ** 2 and a + b + c < x:
                solutions.append([a,b,c])
    return solutions

def maximised_solutions(list1):
    return [sum(i) for i in list1]

x = (maximised_solutions(right_triangles(1000)))
largest = 0
for i in range(min(x),max(x) + 1):
    if x.count(i) > x.count(largest):
        largest = i
print(largest)
