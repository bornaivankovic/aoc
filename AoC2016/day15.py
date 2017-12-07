import numpy
with file("day15.txt",'r') as f:
    strings=f.readlines()

discs={}

def display():
    for i in range(1,len(discs)+1):
        s=""
        for c in discs[i]["array"]:
            s+=c
        print s

def move():
    for i in range(1,len(discs)+1):
        discs[i]["array"]=numpy.roll(discs[i]["array"],1)
        discs[i]["cur_time"]+=1
        discs[i]["cur_time"]=(discs[i]["cur_time"]+1)%len(discs[i]["array"])

def check(pos,disc):
    if discs[disc]["array"][pos]=="o":
        return True
    else:
        return False

def chck(disc):
    if disc>len(discs):
        return True
    a=discs[disc]["array"]
    if a[-disc+1]=="o":
        return True and chck(disc+1)
    else:
        return False and chck(disc+1)


for line in strings:
    split=line.strip().split(" ")
    n_pos=int(split[3])
    pos=int(split[-1][:-1])
    discs[int(split[1][1])]={"array":["x" if i!=pos else "o" for i in range(n_pos) ],"cur_time":0,"cur_pos":pos}


time=0
while not chck(1):
    time+=1
    move()

display()
print time-1
    


