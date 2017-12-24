with file("day24.txt","r") as f:
    ports=[tuple([int(y) for y in x.strip().split("/")]) for x in f.readlines()]

start=filter(lambda x:x[0]==0 or x[1]==0,ports)

def bridge_str(b):
    tmp=0
    for i in b:
        tmp+=i[0]+i[1]
    return tmp

def get_next_ports(b):
    if len(b)>=2:
        cur=b[-1][0] if b[-2][0]==b[-1][1] or b[-2][1]==b[-1][1] else b[-1][1]
    else:
        cur=b[-1][0] if b[-1][1]==0 else b[-1][1]
    return filter(lambda x:x[0]==cur or x[1]==cur,list(set(ports)-set(b)))

br=[]
for i in start:
    bridges=[(i,)]
    cur=0

    while True:
        if cur==len(bridges):
            break
        next_ports=get_next_ports(bridges[cur])
        if not next_ports:
            cur+=1
            continue
        for j in next_ports:
            bridges.append(bridges[cur]+(j,))
        cur+=1
    br.extend(bridges)
"""
part1
"""
strengths=[bridge_str(x) for x in br]
print max(strengths)

"""
part2
"""
max_l=max([len(x) for x in br])
print max([bridge_str(x) for x in filter(lambda x:len(x)==max_l,br)])