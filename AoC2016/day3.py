from itertools import permutations
with file("day3.txt",'r') as f:
    strings=f.readlines()

k=0
triangles=[[],[],[]]
for line in strings:
    split=map(int,line.split())
    sides=[]
    for i in range(len(split)):
        triangles[i].append(split[i])
        sides.append(split[i])
    j=0
    for perm in permutations(sides):
        if perm[0]>=(perm[1]+perm[2]):
            j+=1
    if j>0:
        k+=1
pos=0
for i in triangles:
    start=0
    stop=2
    inc=3
    while stop<=len(i):
        if (i[start]+i[start+1])>i[stop] and (i[start]+i[stop])>i[start+1] and (i[start+1]+i[stop])>i[start]:
            pos+=1
        start+=inc
        stop+=inc



print len(strings)-k
print pos
