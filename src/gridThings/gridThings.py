import numpy as np
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

grids = {}

def create(id, w, h):
    grid = np.array([],[])
    grid.resize(h,w)
    grids[str(id)] = grid
    for i in range(len(grid)):
        for x in range(len(grid[i])):
            grid[i][x] = None

def add(id, x, y, val):
    i = grids[str(id)]
    i[y][x] = val

def height(id):
    i = grids[str(id)]
    return len(i)

def width(id):
    i = grids[str(id)]
    return len(i[0])

def findFirst(id, val):
    grid = grids[str(id)]
    for y in range(height(id) - 1):
        row = grid[y]
        for x in range(width(id) - 1):
            if row[x] == val:
                return [x, y]
    
    return 0

def contains(id, val):
    grid = grids[str(id)]
    for y in range(height(id) - 1):
        row = grid[y]
        for x in range(width(id) - 1):
            if row[x] == val:
                return True
    
    return False

def findAmmount(id, val):
    num = 0
    grid = grids[str(id)]
    for y in range(height(id) - 1):
        row = grid[y]
        for x in range(width(id) - 1):
            if row[x] == val:
                num += 1
    
    return num

def findRow(id, r, val):
    grid = grids[str(id)]
    row = grid[r]
    for i in row:
        if row[i] == val:
            return i
    
    return False


def findCol(id, c, val):
    grid = grids[str(id)]
    for i in grid:
        if grid[c] == val:
            return i
    
    return False

def findPos(id, x, y):
    grid = grids[str(id)]
    return grid[y][x]

def destroy(id):
    grids[id].pop()