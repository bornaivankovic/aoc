import re
with file("day7.txt",'r') as file:
    strings=file.readlines()

wires={}
wires2={}
def parse_line(line):
    split=re.split(" -> ",line.strip())
    if wires.get(split[1]) ==None:
        wires[split[1]]=[split[0]]
    else:
        wires[split[1]].append(split[0])

def update_value(wire,value):
    global wires,wires2
    wires2[wire]=value
    for i in wires.keys():
        res=re.search("^"+wire+"{1} | "+wire+"{1}$",wires[i][0])
        if res!=None:
            respos = res.end()-1
            if respos<=len(wire):
                end=len(wires[i][0])
                wires[i][0]=str(value)+wires[i][0][respos:end]
            else:
                wires[i][0]=wires[i][0][0:respos-(len(wire)+1)%2]+str(value)
            

def evaluate():
    changed=0
    value=None
    for i in wires.keys():
        split=re.split(" ",wires[i][0])
        if len(split)==3:
            l=split[0]
            op=split[1]
            r=split[2]
            if l.isdigit() and r.isdigit():
                    if op=="AND":
                        value=int(l)&int(r)
                        update_value(i,value)
                        wires[i][0]=str(value)
                        changed+=1                        
                    elif op=="OR":
                        value=int(l)|int(r)
                        update_value(i,value)
                        wires[i][0]=str(value)
                        changed+=1
                    elif op=="LSHIFT":
                        value=int(l)<<int(r)
                        update_value(i,value)
                        wires[i][0]=str(value)
                        changed+=1
                    elif op=="RSHIFT":
                        value=int(l)>>int(r)
                        update_value(i,value)
                        wires[i][0]=str(value)
                        changed+=1
        elif len(split)==2:
            if split[1].isdigit():
                value=~int(split[1])& 0xffff
                update_value(i,value)
                wires[i][0]=str(value)
                changed+=1
        elif wires[i][0]:
            if split[0].isdigit():
                value=int(split[0])
                update_value(i,value)
                wires[i][0]=str(value)
                changed+=1
        if value!=None:
            wires2[i]=value
    return changed

    

for line in strings:
    parse_line(line)
for i in wires.keys():
    wires2[i]=-1

while True:
    a=evaluate()
    if a==len(wires.keys())-1:
        break
print wires["lw"],wires["lx"],wires["a"]

