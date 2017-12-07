from __future__ import print_function
from collections import deque

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

def find_path_bfs(maze,dst):
    start, goal = (1, 1), dst
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

inp=1352
#inp=10
start=(1,1)
dst=(39,31)
#dst=(4,7)

def formula(tup):
    x=tup[0]
    y=tup[1]
    return x*x + 3*x + 2*x*y + y + y*y

def bit_number(x):
    b=bin(x)
    b=b.split('b')[1]
    i=0
    for x in b:
        if x=="1":
            i+=1
    return i

def display(display):
    for i in range(len(display)):
        for j in range(len(display[i])):
            print(display[i][j],end="")
        print()

l=50
office=[["." for i in range(l)]for j in range(l)]
cur=start
for i in range(l):
    for j in range(l):
        cur=(i,j)
        num=formula(cur)
        num+=inp
        if bit_number(num)%2==1:
            office[j][i]="#"

cnt=0
for i in range(l):
    for j in range(l):
        dst=(i,j)
        x=find_path_bfs(office,dst)
        if x!="NO WAY!" and len(x)<=50:
            cnt+=1
print(cnt)



