with file("day23.txt","r") as f:
    lines=[x.strip() for x in f.readlines()]


"""
part1
"""
reg={"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0}
cur=0
cnt=0
i=[0 for x in range(33)]
def val(x):
    if reg.get(x)!=None:
        return reg[x]
    else: return int(x)
while True:
    i[cur]+=1
    try:
        ins=lines[cur]
        ins=ins.split()
        if "set" in ins:
            reg[ins[1]]=val(ins[2])
        elif "sub" in ins:
            reg[ins[1]]-=val(ins[2])
        elif "mul" in ins:
            reg[ins[1]]*=val(ins[2])
            cnt+=1
        elif "jnz" in ins:
            if val(ins[1])!=0:
                cur+=val(ins[2])
                continue
        cur+=1
    except :
        print cnt
        break

"""
part2
"""
h=0
for x in range(105700,122700 + 1,17):
    for i in range(2,x):
        if x%i==0:
            h+=1
            break
print h