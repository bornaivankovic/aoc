from itertools import combinations
with file("day17.txt","r") as f:
    containers=[int(x.strip()) for x in f.readlines()]

inp=150
cnt=0
m=len(containers)
for i in range(len(containers)):
    for j in combinations(containers,i):
        if sum(j)==inp:
            if i<m: m=i
            cnt+=1
print cnt

cnt=0
for i in combinations(containers,m):
    if sum(i)==inp:
        cnt+=1
print cnt