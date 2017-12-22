from operator import add
with file("day22.txt","r") as f:
    lines=[x.strip() for x in f.readlines()]

# lines=[
#     "..#",
#     "#..",
#     "...",
# ]
#(x,y,facing) facing=0-north,1-east,2-south,3-west
dirs=[(0,-1),(1,0),(0,1),(-1,0)]
cur=(len(lines)/2,len(lines[0])/2,0)
cnt=0
def burst():
    global lines,cur,cnt
    if lines[cur[1]][cur[0]]==".":
        cur=(cur[0],cur[1],(cur[2]-1)%4)
        tmp=lines[cur[1]]
        lines[cur[1]]=tmp[:cur[0]]+"W"+tmp[cur[0]+1:]
    elif lines[cur[1]][cur[0]]=="#":
        cur=(cur[0],cur[1],(cur[2]+1)%4)
        tmp=lines[cur[1]]
        lines[cur[1]]=tmp[:cur[0]]+"F"+tmp[cur[0]+1:]
    elif lines[cur[1]][cur[0]]=="F":
        cur=(cur[0],cur[1],(cur[2]+2)%4)
        tmp=lines[cur[1]]
        lines[cur[1]]=tmp[:cur[0]]+"."+tmp[cur[0]+1:]
    elif lines[cur[1]][cur[0]]=="W":
        tmp=lines[cur[1]]
        lines[cur[1]]=tmp[:cur[0]]+"#"+tmp[cur[0]+1:]
        cnt+=1

    cur=(cur[0]+dirs[cur[2]][0],cur[1]+dirs[cur[2]][1],cur[2])

def expand():
    global lines,cur
    for i in range(len(lines)):
        lines[i]="."+lines[i]+"."
    lines.insert(0,"."*len(lines[0]))
    lines.append("."*len(lines[0]))
    cur=(cur[0]+1,cur[1]+1,cur[2])

for k in range(10000000):
    if cur[0]==0 or cur[0]==len(lines) or cur[1]==0 or cur[1]==len(lines):
        expand()
    burst()
    # print cur
# for i in lines:
#     print i

print cnt




