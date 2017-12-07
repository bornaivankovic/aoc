from itertools import permutations
with file("day2.txt","r") as f:
    lines=f.readlines()
    lines=[x.strip() for x in lines]


rows=[]
"""
part 1
"""
# for i in lines:
#     split=i.split("\t")
#     split=[int(x) for x in split]
#     rows.append(max(split)-min(split))

"""
part 2
"""
for i in lines:
    split=i.split("\t")
    split=[int(x) for x in split]
    for (j,k) in permutations(split,2):
        if j%k==0:
            rows.append(j/k)

print sum(rows)