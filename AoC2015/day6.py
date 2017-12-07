import re
with file("day6.txt",'r') as file:
    strings=file.readlines()
lights= [[0 for x in range(1000)] for y in range(1000)] 

def change_lights(opcija,x1,y1,x2,y2):
    global lights
    a=range(x1,x2)
    b=range(y1,y2)
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            if(opcija=="toggle"):
                lights[i][j]+=2
            if(opcija=="on"):
                lights[i][j]+=1
            if(opcija=="off"):
                if lights[i][j]==0:
                    continue
                else:
                    lights[i][j]-=1

for line in strings:
    if re.search("toggle",line):
        opcija="toggle"
    if re.search("turn off",line):
        opcija="off"
    if re.search("turn on",line):
        opcija="on"
    split=re.split("through",line,1)
    tmp=re.split(" ",split[0].strip(),1)
    tmp=re.split(" ",tmp[1])
    if len(tmp)>1:
        s=tmp[1]
    else:
        s=tmp[0]
    x1= int(re.split(",",s)[0])
    y1= int(re.split(",",s)[1])
    x2= int(re.split(",",split[1].strip())[0])
    y2= int(re.split(",",split[1].strip())[1])
    change_lights(opcija,x1,y1,x2,y2)

x=0
for i in range(1000):
    for j in range(1000):
        x+=lights[i][j]
print x