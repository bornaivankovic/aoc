import math
inp=361527

NORTH, S, W, E = (0, 1), (0, -1), (-1, 0), (1, 0) 
turn_right = {NORTH: E, E: S, S: W, W: NORTH} 
dirs=[NORTH,S,W,E,(1,1),(1,-1),(-1,1),(-1,-1)]


"""
part1
"""
def spiral(width, height):
    if width < 1 or height < 1:
        raise ValueError
    x, y = width // 2, height // 2 
    dx, dy = NORTH 
    matrix = [[None] * width for _ in range(height)]
    count = 0
    while True:
        count += 1
        matrix[y][x] = count # visit
        # try to turn right
        new_dx, new_dy = turn_right[dx,dy]
        new_x, new_y = x + new_dx, y + new_dy
        if (0 <= new_x < width and 0 <= new_y < height and
            matrix[new_y][new_x] is None): # can turn right
            x, y = new_x, new_y
            dx, dy = new_dx, new_dy
        else: # try to move straight
            x, y = x + dx, y + dy
            if not (0 <= x < width and 0 <= y < height):
                return matrix # nowhere to go

def print_matrix(matrix):
    width = len(str(max(el for row in matrix for el in row if el is not None)))
    fmt = "{:0%dd}" % width
    for row in matrix:
        print(" ".join("_"*width if el is None else fmt.format(el) for el in row))
        
def find_element(x,spiral):
    cord=(-1,-1)
    for i in range(len(spiral)):
        row=[int(j) for j in spiral[i]]
        if x in row:
            for j in range(len(row)):
                if row[j]==x:
                    cord=(j,i)
    return cord

def manhattan_distance(start,end):
    return abs(end[0] - start[0]) + abs(end[1] - start[1])

dim=int(math.ceil(math.sqrt(inp)))
dim=dim if dim%2==1 else dim+1
sp=spiral(dim,dim)
print manhattan_distance(find_element(inp,sp),(dim/2,dim/2))

"""
part 2
"""
def spiral2(width, height):
    if width < 1 or height < 1:
        raise ValueError
    x, y = width // 2, height // 2 
    dx, dy = NORTH 
    matrix = [[None] * width for _ in range(height)]
    while True:
        if (x,y)==(width/2,height/2):
            matrix[y][x]=1
        else:
            visited=[]
            for i in dirs:
                try:
                    cur_cell=matrix[y+i[1]][x+i[0]]
                    if cur_cell!= None:
                        visited.append(cur_cell)
                except:
                    pass
            s=sum(visited)
            if s>inp:
                print s
                return
            matrix[y][x] = s
        # try to turn right
        new_dx, new_dy = turn_right[dx,dy]
        new_x, new_y = x + new_dx, y + new_dy
        if (0 <= new_x < width and 0 <= new_y < height and
            matrix[new_y][new_x] is None): # can turn right
            x, y = new_x, new_y
            dx, dy = new_dx, new_dy
        else: # try to move straight
            x, y = x + dx, y + dy
            if not (0 <= x < width and 0 <= y < height):
                return matrix # nowhere to go

spiral2(dim,dim)