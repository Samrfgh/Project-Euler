
def perm(list1):
    if len(list1) == 1:
        yield list1
    else:
        plist = []
        for i in range(len(list1)):
            x = list1[i]
            y = list1[:i] + list1[i + 1:]
            for a in perm(y):
                yield [x] + a

list9 = [0,1,2,3,4,5,6,7,8,9]

def answer(digits, nth):
    for i,v in enumerate(perm(digits)):
        if i == nth:
            return v

print(answer(list9,999999))
# from itertools import permutations
# l = list(permutations(range(10)))
# print(l[999999])
