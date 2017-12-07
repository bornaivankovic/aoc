from hashlib import md5
from itertools import product
inp="njfxhljp"
allowed="bcdef"

def try_find_path(path):
    n=0
    cur=(0,0)
    for i in range(len(path)):
        if n!=i or cur[0]>3 or cur[0]<0 or cur[1]>3 or cur[1]<0:
            break
        hashed=md5(inp+path[:i]).hexdigest()
        if hashed[0] in allowed and path[i]=="U":
            cur=(cur[0],cur[1]-1)
            n+=1
        if hashed[1] in allowed and path[i]=="D":
            cur=(cur[0],cur[1]+1)
            n+=1
        if hashed[2] in allowed and path[i]=="L":
            cur=(cur[0]-1,cur[1])
            n+=1
        if hashed[3] in allowed and path[i]=="R":
            cur=(cur[0]+1,cur[1])
            n+=1
    if n==len(path) and cur[0]==3 and cur[1]==3:
        return n
    else:
        return 1000000

flag=False
for i in range(6,20):
    if flag:
        break
    combs=product("UDLR",repeat=i)
    for j in combs:
        p="".join(j)
        x=try_find_path(p)
        if x==len(p):
            print p
            flag=True
            break


