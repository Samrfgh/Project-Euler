def load_file(filename):
    f = open(filename, "r")
    return f.readlines()

def sudoku():
    sudoku_grids = []
    grid = []
    for i in load_file("/Users/sam/Desktop/python/Project Euler/p096_sudoku.txt"):
        if i[0:4] == 'Grid':
            continue
        else:
            grid.append(list(i.strip('\n')))
            if len(grid) == 9:
                sudoku_grids.append(grid)
                grid = []
    return sudoku_grids

def columns_of_grid(grid,y):
    a_column = []
    for i in grid:
        a_column.append(i[y])
        #print(a_column)
    return a_column

def squares_of_grid(grid):
    squares = []
    for i in range(0,9,3):
        a_square = []
        for a in grid:
            a_square += a[i:i + 3]
            if len(a_square) == 9:
                squares.append(a_square)
                a_square = []
                continue
    return squares

def which_square(lst,x,y):
    if x < 3 and y < 3:
        return lst[0]
    elif x < 6 and y < 3:
        return lst[1]
    elif x < 9 and y < 3:
        return lst[2]
    elif x < 3 and y < 6:
        return lst[3]
    elif x < 6 and y < 6:
        return lst[4]
    elif x < 9 and y < 6:
        return lst[5]
    elif x < 3 and y < 9:
        return lst[6]
    elif x < 6 and y < 9:
        return lst[7]
    elif x < 9 and y < 9:
        return lst[8]

def how_many_options(grid,x,y):
    lst = [0,1,2,3,4,5,6,7,8,9]
    rcs = (columns_of_grid(grid,y)) + (grid[x]) + (which_square(squares_of_grid(grid),x,y))
    for i in set(rcs):
        lst.remove(int(i))
    return [len(lst),lst]

def fill_a_space(grid,x,y):
    a = how_many_options(grid,x,y)
    if a[0] == 1:
        grid[x][y] = str(a[1][0])
    elif a[0] == 0:
        return 'incorrect'
    return grid

def iterate(grid):
    for a in range(len(grid)):
        for b in range(len(grid[a])):
            if grid[a][b] == '0':
                x = fill_a_space(grid,a,b)
                if x == 'incorrect':
                    return 'error'
                else:
                    x
    return grid

def is_solved(grid):
    for i in grid:
        for j in i:
            if j == '0':
                return False
    return True

def least_options(grid):
    smallest = [0,0,9,[]]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '0':
                x = how_many_options(grid,i,j)
                if x[0] < smallest[2]:
                    smallest = [i,j,x[0],x[1]]
                    if smallest[2] == 1:
                        return smallest
    return smallest

def grid_copy(grid):
    new_grid = []
    for i in grid:
        new_grid.append(i[:])
    return new_grid

def fill_a_grid(grid):
    x = 0
    while x < 81:
        z = iterate(grid)
        if z == 'error':
            return None
        elif least_options(z)[2] != 1:
            break
        x += 1
    if is_solved(grid):
        return int(''.join(grid[0][0:3]))
    else:
        y = least_options(grid)
        for i in y[3]:
            a = grid_copy(grid)
            a[y[0]][y[1]] = str(i)
            #print(y,a)
            f = fill_a_grid(a)
            #print('f',f)
            if f != None :
                return f


#PROBLEM IS IN THE FILL_A_GRID SECTION, ANY LAYER COULD BE INCORRECT. ONCE TOP LEVEL IS INCORRECT PYTHON WILL RETURN NONE.
def answer():
    x = 0
    for i in sudoku():
        y = fill_a_grid(i)
        x += y
    return x


print(answer())
#print(least_options([['0', '0', '3', '0', '2', '0', '6', '0', '0'], ['9', '0', '0', '3', '0', '5', '0', '0', '1'], ['0', '0', '1', '8', '0', '6', '4', '0', '0'], ['0', '0', '8', '1', '0', '2', '9', '0', '0'], ['7', '0', '0', '0', '4', '0', '0', '0', '8'], ['0', '0', '6', '7', '0', '8', '2', '0', '0'], ['0', '0', '2', '6', '0', '9', '5', '0', '0'], ['8', '0', '0', '2', '0', '3', '0', '0', '9'], ['0', '0', '5', '0', '1', '0', '3', '0', '0']]))
#print(fill_a_grid(sudoku()[1]))
#print(sudoku()[49][8])
