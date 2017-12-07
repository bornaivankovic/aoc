from itertools import permutations,combinations
with file("day4.txt","r") as f:
    lines=f.readlines()
    lines=[x.strip() for x in lines]

"""
part1
"""
valid=[]
for i in lines:
    split=i.split(" ")
    cnt=len(split)
    for j in range(len(split)):
        a=split[j]
        b=split[:j]+split[j+1:]
        if a not in b:
            cnt-=1
    if cnt==0:
        valid.append(i)

print len(valid)
"""
part2
"""
def check_if_anagram(source_word,target_word):
    perms=list(permutations(source_word))
    for i in perms:
        if "".join(i) == target_word:
            return True
    return False


valid=[]
for i in lines:
    split=i.split(" ")
    cnt=0
    for j in combinations(split,2):
        if check_if_anagram(j[0],j[1]):
            cnt+=1        
    if cnt==0:
        valid.append(i)

print len(valid)