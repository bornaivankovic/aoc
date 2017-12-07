from collections import deque
from itertools import permutations
with file("day24.txt",'r') as f:
    lines=f.readlines()

lines=[l.strip() for l in lines]
#lines=["###########","#0.1.....2#","#.#######.#","#4.......3#","###########"]

nodes={}

def maze2graph(maze):
    height = len(maze)
    width = len(maze[0]) if height else 0
    graph = {(i, j): [] for j in range(width) for i in range(height) if  maze[i][j]!="#"}
    for row, col in graph.keys():
        if row < height - 1 and maze[row + 1][col]!="#":
            graph[(row, col)].append(("S", (row + 1, col)))
            graph[(row + 1, col)].append(("N", (row, col)))
        if col < width - 1 and maze[row][col + 1]!="#":
            graph[(row, col)].append(("E", (row, col + 1)))
            graph[(row, col + 1)].append(("W", (row, col)))
    return graph

def find_path_bfs(maze,src,dst):
    start, goal = src, dst
    queue = deque([("", start)])
    visited = set()
    graph = maze2graph(maze)
    while queue:
        path, current = queue.popleft()
        if current == goal:
            return path
        if current in visited:
            continue
        visited.add(current)
        for direction, neighbour in graph[current]:
            queue.append((path + direction, neighbour))
    return "NO WAY!"

def get_dst(p):
    dst=0
    for i in range(len(p)-1):
        pa=paths[(p[i],p[i+1])]
        dst+=len(pa)
    return dst

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j].isdigit():
            nodes[int(lines[i][j])]=(i,j)
paths={}
for i in permutations(nodes,2):
    p=find_path_bfs(lines,nodes[i[0]],nodes[i[1]])
    paths[i]=p
dst={}

for i in permutations(nodes):
    if i[0]!=0:
        continue
    a=list(i)
    a.append(0)
    dst[i]=get_dst(a)

print min(dst.values())

