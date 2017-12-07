from collections import deque
from itertools import permutations
with file("day21.txt",'r') as f:
    lines=f.readlines()
    
inp="abcdefgh"
for i in permutations("abcdefgh"):
    inp="".join(i)
    for line in lines:
        split=line.strip().split(" ")
        if len(inp)!=len("abcdefgh"):
            print line
        if split[0]=="rotate":
            if split[1]=="based":
                n=inp.index(split[-1])
                if n>=4:
                    n+=2
                else:
                    n+=1
                inp=deque(inp)
                inp.rotate(n)
                inp="".join(inp)
            else:
                n=int(split[-2])
                if split[1]=="left":
                    n*=-1
                inp=deque(inp)
                inp.rotate(n)
                inp="".join(inp)
        if split[0]=="swap":
            if split[1]=="position":
                x=int(split[2])
                y=int(split[-1])
                
            else:
                x=inp.index(split[2])
                y=inp.index(split[-1])
            if x<y:
                inp=inp[:x]+inp[y]+inp[x+1:y]+inp[x]+inp[y+1:]
            else:
                inp=inp[:y]+inp[x]+inp[y+1:x]+inp[y]+inp[x+1:]
        if split[0]=="move":
            l=inp[int(split[2])]
            d=int(split[-1])
            inp=inp.replace(l,"")
            inp=inp[:d]+l+inp[d:]
        if split[0]=="reverse":
            x=int(split[2])
            y=int(split[-1])
            if x==0:
                rev=inp[y::-1]
            else:
                rev=inp[y:x-1:-1]
            inp=inp[:x]+rev+inp[y+1:]

    if inp=="fbgdceah":
        print "".join(i)
        break


