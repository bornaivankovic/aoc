from day10 import knot_hash
import operator
# inp="flqrgnkx"
inp="jxqlasbh"

dirs=[(0,1),(0,-1),(1,0),(-1,0)]

def mark_group(start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            neighbourhood=set()
            for i in dirs:
                try:
                    tmp=tuple(map(operator.add,vertex,i))
                    if tmp[0]<0 or tmp[1]<0: continue
                    if hashes[tmp[0]][tmp[1]]=="1" and tmp not in visited :neighbourhood.add(tmp)
                except:
                    pass
            queue.extend(list(neighbourhood))
    return visited
        

hash_inputs=[[ord(j) for j in i] for i in [inp+"-"+str(x) for x in range(128)]]
hashes=['{:0128b}'.format(int(knot_hash(i),16)) for i in hash_inputs]

"""
part1
"""
cnt=0
for i in hashes:
    cnt+=i.count("1")
print cnt

"""
part2
"""
cnt2=0
for i in range(len(hashes)):
    for j in range(len(hashes[i])):
        if hashes[i][j]=="1":
            grp=mark_group((i,j))
            for k in grp:
                hashes[k[0]]=hashes[k[0]][:k[1]]+"2"+hashes[k[0]][k[1]+1:]
            cnt2+=1
print cnt2
