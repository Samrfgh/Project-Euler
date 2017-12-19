def simplifyed_fractions(x,y):
    hcf = 0
    for i in range(1,x + 1):
        if x % i == 0 and y % i ==0:
            hcf = i
    return [x / hcf, y / hcf]

def digitcancelling_fractions(x,y):
    if x % 10 != 0 and y % 10 != 0:
        s = set(str(x)).intersection(set(str(y)))
        if len(s) == 1:
            i = list(str(x))
            j = list(str(y))
            i.remove(list(s)[0])
            j.remove(list(s)[0])
            if simplifyed_fractions(int(i[0]),int(j[0])) == simplifyed_fractions(x,y):
                return [x,y]
    return []

def list_of_digitcancelling_fractions(x,y):
    list1 = []
    for i in range(x,y):
        for j in range(x + 1,y):
            if i > j or i == j:
                continue
            else:
                if len(digitcancelling_fractions(i,j)) == 2:
                    list1.append(digitcancelling_fractions(i,j))
    return list1

def product(list1):
    numerator = []
    denomonator = []
    for i in list1:
        numerator.append(i[0])
        denomonator.append(i[1])
    p1 = 1
    for a in numerator:
        p1 *= a
    p2 = 1
    for b in denomonator:
        p2 *= b
    return simplifyed_fractions(p1,p2)[1]

print(product(list_of_digitcancelling_fractions(10,100)))
