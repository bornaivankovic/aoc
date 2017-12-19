import operator
with file("day18.txt","r") as f:
    lines=[x.strip() for x in f.readlines()]

dirs=[(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]
lights=[]
for line in lines:
    lights.append([x for x in line])

def corners_on():
    lights[0][0],lights[-1][0],lights[0][-1],lights[-1][-1]="#","#","#","#"


def step():
    change=[]
    for i in range(len(lights)):
        for j in range(len(lights[i])):
            on=0
            for k in dirs:
                try:
                    tmp=tuple(map(operator.add,(i,j),k))
                    if tmp[0]<0 or tmp[1]<0: continue
                    if lights[tmp[0]][tmp[1]]=="#": on+=1
                except:
                    pass
            if lights[i][j]=="#" and not(2<=on<=3): change.append((i,j))
            elif lights[i][j]=="." and on==3: change.append((i,j))
    for i in change:
        if lights[i[0]][i[1]]=="#": lights[i[0]][i[1]]="."
        else: lights[i[0]][i[1]]="#"

corners_on()
for i in range(100):
    step()
    corners_on()

cnt=0
for i in lights:
    for j in i:
        if j=="#": cnt+=1

print cnt

        
