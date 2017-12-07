import re
import json
with file("day12.txt",'r') as file:
    strings=file.readlines()

def n(j):
    if type(j) == int:
        return j
    if type(j) == list:
        return sum([n(j) for j in j])
    if type(j) != dict:
        return 0
    if 'red' in j.values():
        return 0
    return n(list(j.values()))

a= json.loads(strings[0].strip())
print n(a)


