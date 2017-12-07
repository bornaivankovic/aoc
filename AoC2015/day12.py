import re
with file("day12.txt",'r') as file:
    strings=file.readlines()
    
res=re.findall("(-?[0-9]+)",strings[0])
j=0
for i in res:
    j+=int(i)
print j