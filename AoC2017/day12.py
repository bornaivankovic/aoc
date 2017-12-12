with file("day12.txt","r") as f:
    lines=[x.strip() for x in f.readlines()]

def get_group(grp_id):
    visited, queue = set(), [grp_id]
    while queue:
        current = queue.pop(0)
        if current not in visited:
            visited.add(current)
            queue.extend(set(pipes[current]) - visited)
    return visited


pipes={}
for line in lines:
    split=line.split(" <-> ")
    pipes[int(split[0])]=[int(x) for x in split[1].split(", ")]

"""
part1
"""
g=get_group(0)
print len(g)

"""
part2
"""
cnt=1
while True:
	tmp=set(pipes.keys())-g
	if not tmp:
		break
	g=set(list(g)+list(get_group(list(tmp).pop(0))))
	cnt+=1
	
print cnt
	
