with file("day11.txt",'r') as f:
    strings=f.readlines()

generators={}
microchips={}

def display_floors():
    for i in range(len(floors)-1,-1,-1):
        s=""
        for j in range(len(floors[i])):
            s+=floors[i][j]+"\t"
        print s

def check(i):
    if i>len(floors[3])-1: return True
    if floors[3][i]!=".": return True and check(i+1)
    else: return False

for line in range(len(strings)):
    split=strings[line].strip().split(" ")
    for i in range(len(split)):
        if split[i].startswith("generator"):
            generators[split[i-1][0]]=line+1
        if split[i].startswith("microchip"):
            microchips[split[i-1][0]]=line+1

floors=[["." for i in range(2*len(generators)+2)]for j in range(4)]
for i in range(len(floors)):
    floors[i][0]="F"+str(i+1)

floors[0][1]="E"
for i in range(len(generators)):
    k=generators.keys()[i]
    f=generators[k]-1
    f2=microchips[k]-1
    floors[f][i*2+2]=k.upper()+"G"
    floors[f2][i*2+3]=k.upper()+"M"

display_floors()
#cba writing code so i solved it by hand
