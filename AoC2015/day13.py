from collections import defaultdict
from itertools import permutations
with file("day13.txt", 'r') as file:
    strings = file.readlines()

relations = defaultdict(dict)
people=set()
for i in strings:
    tmp=i.strip()[:-1].split(" ")
    if tmp[2]=="gain":
        value=int(tmp[3])
    else:
        value=-int(tmp[3])
    relations[tmp[0]][tmp[-1]]=value
    people.add(tmp[0])
    people.add(tmp[-1])

people.add("Me")
for p in people:
    relations["Me"][p]=0
    relations[p]["Me"]=0

happines=[]
for perm in permutations(people):
    j=0
    for i in range(len(perm)):
        j+=relations[perm[i%len(perm)]][perm[(i+1)%len(perm)]]+relations[perm[i%len(perm)]][perm[(i-1)%len(perm)]]
    happines.append(j)
print max(happines)
