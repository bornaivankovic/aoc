import numpy as np
with file("day21.txt","r") as f:
    lines=[x.strip() for x in f.readlines()]

# lines=[
#     "../.# => ##./#../...",
#     ".#./..#/### => #..#/..../..../#..#"
# ]
rules=[]
art=((".","#","."),(".",".","#"),("#","#","#"))

def print_art(art):
    s=""
    for i in art:
        for j in i:
            s+=j
        s+="\n"
    print s

def check_rules(inp):
    for i in range(len(rules)):
        left=tuple(tuple(x for x in j) for j in rules[i][0].split("/"))
        if inp==left:
            return i
    return -1

def flip_rotate(art):
    ret=[]
    for i in range(4):
        tmp=np.rot90(art,i)
        ret.append(tuple(map(tuple,tmp)))
        ret.append(tuple(map(tuple,np.flipud(tmp))))
        ret.append(tuple(map(tuple,np.fliplr(tmp))))
    return ret

def split_art(art):
    ret=[]
    n=0
    if len(art)%2==0:n=2
    else:n=3
    for i in np.vsplit(np.array(art),tuple(range(n,len(art),n))):
        tmp=np.hsplit(i,tuple(range(n,len(art),n)))
        for j in tmp:
            ret.append(tuple(map(tuple,j)))
    return ret

def join_art(art):
    tmp=[]
    n=int(len(art)**0.5)
    if n>1:
        for i in range(n):
            tmp.append(np.hstack(art[i*n:(i+1)*n]))
        return tuple(map(tuple,np.vstack(np.stack(tmp))))
    else: return art[0]

for line in lines:
    split=line.split(" => ")
    rules.append((split[0],split[1]))

for z in range(18):
    print z
    art=split_art(art)
    for a in range(len(art)):
        r=-1
        for i in flip_rotate(art[a]):
            r=check_rules(i)
            if r>=0:
                break
        art[a]=tuple(tuple(x for x in j) for j in rules[r][1].split("/"))
    art=join_art(art)
    # print_art(art)

cnt=0
for i in art:
    cnt+=i.count("#")
print cnt