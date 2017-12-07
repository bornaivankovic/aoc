import numpy
with file("day1.txt",'r') as f:
    strings=f.readlines()

split=strings[0].strip().split(", ")
sides=[0,1,2,3]
x,y=0,0
locations=[(0,0)]
flag=False
def new_loc(x,y):
    global locations
    if (x,y) in locations:
        print abs(x)+abs(y)
        return True
    else:
        locations.append((x,y))
        return False
for i in split:
    if flag:
        break
    if i[0]=="R":
        sides=numpy.roll(sides,1)
    else:
        sides=numpy.roll(sides,-1)
    if sides[0]==0:
        for j in range(int(i[1:])):
            y+=1
            new_loc(x,y)
        
    if sides[0]==1:
        for j in range(int(i[1:])):
            x+=1
            new_loc(x,y)
        
    if sides[0]==2:
        for j in range(int(i[1:])):
            y-=1
            new_loc(x,y)
        
    if sides[0]==3:
        for j in range(int(i[1:])):
            x-=1
            new_loc(x,y)
        
    

        
print abs(x)+abs(y)