def integer_combinations(a,b):
    distinct_terms = []
    for x in range(a,b + 1):
        for y in range(a,b + 1):
            distinct_terms.append(x ** y)
    return list(set(distinct_terms))

print(len(integer_combinations(2,100)))
