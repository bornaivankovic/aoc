with file("day23.txt",'r') as f:
    lines=f.readlines()

lines=[l.strip() for l in lines]

loop=["cpy b c","inc a","dec c","jnz c -2","dec d","jnz d -5"]

registers={"a":12,"b":0,"c":0,"d":0}

a=[0 for i in range(len(lines))]

def parse(s):
    if s[0]=="-":
        return -int(s[1:])
    elif s.isdigit():
        return int(s)
    else:
        return s

i=0
while True:
    if(i>len(lines)-1):
        break
    split=lines[i].split(" ")
    inst=split[0]
    p1=parse(split[1])
    if len(split)>2:
        p2=parse(split[2])

    if lines[i:i+len(loop)]==loop:
        registers["a"]=registers["b"]*registers["d"]
        registers["d"]=0
        registers["c"]=0
        i+=len(loop)
        continue

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
                if isinstance(p2,int):
                    i+=p2
                    continue
                else:
                    i+=registers[p2]
                    continue
        else:
            if registers[p1]!=0:
                if isinstance(p2,int):
                    i+=p2
                    continue
                else:
                    i+=registers[p2]
                    continue
    if inst=="tgl":
        if i+registers[p1]>len(lines)-1:
            i+=1
            continue
        cur=lines[i+registers[p1]]
        s=cur.split(" ")
        if len(s)<=2:
            if s[0]=="inc":
                cur="dec "+s[1]
            else:
                cur="inc "+s[1]
        else:
            if s[0]=="jnz":
                cur="cpy "+s[1]+" "+s[2]
            else:
                cur="jnz "+s[1]+" "+s[2]
        lines[i+registers[p1]]=cur
    i+=1

print registers