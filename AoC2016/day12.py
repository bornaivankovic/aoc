with file("day12.txt",'r') as f:
    strings=f.readlines()

registers={"a":0,"b":0,"c":1,"d":0}

def parse(s):
    if s[0]=="-":
        return -int(s[1:])
    elif s.isdigit():
        return int(s)
    else:
        return s

i=0
while True:
    if(i>len(strings)-1):
        break
    split=strings[i].strip().split(" ")
    inst=split[0]
    p1=parse(split[1])
    if len(split)>2:
        p2=parse(split[2])
    if inst=="cpy":
        if isinstance(p1,int):
            registers[p2]=p1
        else:
            registers[p2]=registers[p1]
    if inst=="inc":
        registers[p1]+=1
    if inst=="dec":
        registers[p1]-=1
    if inst=="jnz":
        if isinstance(p1,int):
            if p1!=0:
                i+=p2
                continue
        else:
            if registers[p1]!=0:
                i+=p2
                continue
    i+=1

print registers
