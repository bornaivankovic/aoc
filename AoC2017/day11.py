import operator
with file("day11.txt","r") as f:
    line=f.readline().strip()

n,s,ne,se,nw,sw=(0,-1),(0,1),(1,-1),(1,0),(-1,0),(-1,1)

grid={}
split=line.split(",")
cur=(0,0)
grid[cur]=0
for i in split:
    move=vars().get(i)
    val=grid[cur]
    cur=tuple(map(operator.add,cur,move))
    if grid.get(cur) is None:
        grid[cur]=max(abs(cur[0]),abs(cur[1]))

"""
part1
"""
print grid[cur]
"""
part2
"""
print max(grid.values())