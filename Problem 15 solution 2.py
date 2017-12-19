dict1 = {}

def lattice_paths(x,y):
    if (x,y) in dict1:
        return dict1[(x,y)]
    elif x == y == 0:
        dict1[(x,y)] = 1
    elif x == 0:
        dict1[(x,y)] = lattice_paths(x,y - 1)
    elif y == 0:
        dict1[(x,y)] = lattice_paths(x - 1,y)
    else:
        dict1[(x,y)] = lattice_paths(x - 1, y) + lattice_paths(x, y - 1)
    return dict1[ (x,y) ]

print(lattice_paths(20,20))
