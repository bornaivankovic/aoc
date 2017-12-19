from operator import add
with file("day19.txt","r") as f:
    lines=[x for x in f.readlines()]

def char(x):
    return lines[x[1]][x[0]]

cur=(lines[0].index("|"),0)
orient=(0,1)
letters=""
cnt=0
while True:
    try:
        while char(cur)!="+":
            cnt+=1
            if char(cur).isalnum(): 
                letters+=char(cur)
            cur=tuple(map(add,cur,orient))
        if orient==(0,1) or orient==(0,-1):
            try:
                orient=(-1,0) if char(tuple(map(add,cur,(-1,0))))=="-" else (1,0)
            except:
                orient=(1,0)
            cur=tuple(map(add,cur,orient))
        else:
            try:
                orient=(0,1) if char(tuple(map(add,cur,(0,1))))=="|" else (0,-1)
            except:
                orient=(0,-1)
            cur=tuple(map(add,cur,orient))
        cnt+=1
    except:
        print letters,cnt
        break
    