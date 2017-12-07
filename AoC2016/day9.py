import re
with file("day9.txt",'r') as f:
    string=f.read()

asdf="X(8x2)(3x3)ABCY"
line=string.strip()
#line=asdf
res=re.finditer("(\([0-9]+x[0-9]+\))",line)
cur=0
line2=""
for i in res:
    marker=(int(i.group().split("x")[0][1:]),int(i.group().split("x")[1][:-1]))
    span=i.span()
    if(span[0]<cur):
        continue
    line2+=line[cur:span[0]]    
    decomp=line[span[1]:span[1]+marker[0]]*marker[1]
    line2+=decomp
    cur=span[1]+marker[0]
if cur<len(line):
    line2+=line[cur:]
print len(line2)
    
