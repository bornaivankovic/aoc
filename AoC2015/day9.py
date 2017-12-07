from collections import defaultdict
from itertools import permutations
with file("day9.txt", 'r') as file:
    strings = file.readlines()

asdf = ["London to Dublin = 464",
        "London to Belfast = 518",
        "Dublin to Belfast = 141"]
edges = defaultdict(dict)
cities = set()

for line in strings:
    line = line.strip()
    split = line.split(" to ")
    split2 = split[1].split(" = ")
    edges[split[0]][split2[0]]= int(split2[1])
    edges[split2[0]][split[0]]= int(split2[1])
    cities.add(split[0])
    cities.add(split2[0])

dist=[]

for perm in permutations(cities):
    dist.append(sum(map(lambda x, y: edges[x][y], perm[:-1], perm[1:])))

print min(dist),max(dist)