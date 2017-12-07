from itertools import chain,permutations,product
with file("day22.txt",'r') as f:
    lines=f.readlines()

class node:
    def __init__(self,size,used,avail,up,coords):
        self.size=size
        self.used=used
        self.avail=avail
        self.up=up
        self.coords=coords

    def viable_pair(self,n):
        if self.used!=0 and self.used<=n.avail and self!=n:
            return True
        else:
            return False

    def __repr__(self):
        return "["+str(self.coords[0])+","+str(self.coords[1])+"]:"+"U:"+str(self.used)+",A:"+str(self.avail)

    def move_data(self,n):
        self.avail+=self.used
        n.avail-=self.used
        n.used+=self.used
        self.used=0

    
def find_node(coords):
    for i in nodes:
        if i.coords==coords:
            return i
def find_empty_node():
    for i in nodes:
        if i.used==0:
            return i


nodes=[]
for i in range(len(lines)):
    if i<=1:
        continue
    split=lines[i].strip().split(" ")
    split=filter(lambda x:x!="",split)
    coords=split[0].split("-")
    coords=(int(coords[-2][1:]),int(coords[-1][1:]))
    size=int(split[1][:-1])
    used=int(split[2][:-1])
    avail=int(split[3][:-1])
    up=int(split[4][:-1])
    nodes.append(node(size,used,avail,up,coords))
cnt=0
for i in permutations(nodes,2):
    if i[0].viable_pair(i[1]):
        cnt+=1

for i in range(30):
    s=""
    for j in range(33):
        n=find_node((j,i))
        if i==0 and j==0:
            s+="()|"
        elif n.up==0:
            s+="__|"
        elif n.up==100 or n.used>94:
            s+=" #|"
        elif j==32 and i==0:
            s+=" G"
        else:
            s+=str(n.used)+"|"
    print s









    