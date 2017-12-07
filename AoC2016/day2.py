with file("day2.txt",'r') as f:
    strings=f.readlines()

asdf=["ULL","RRDDD","LURDL","UUUUD"]
keypad=[[0,0,1,0,0],[0,2,3,4,0],[5,6,7,8,9],[0,'A','B','C',0],[0,0,'D',0,0]]
cur=(2,0)    
def move(x):
    global cur
    if x=="R":
        if cur[1]==len(keypad[cur[0]])-1 or keypad[cur[0]][cur[1]+1]==0:
            pass
        else:
            cur=(cur[0],cur[1]+1)
    if x=="L":
        if cur[1]==0 or keypad[cur[0]][cur[1]-1]==0:
            pass
        else:
            cur=(cur[0],cur[1]-1)
    if x=="U":
        if cur[0]==0 or keypad[cur[0]-1][cur[1]]==0:
            pass
        else:
            cur=(cur[0]-1,cur[1])
    if x=="D":
        if cur[0]==len(keypad)-1 or keypad[cur[0]+1][cur[1]]==0:
            pass
        else:
            cur=(cur[0]+1,cur[1])


for line in strings:
    for c in line:
        move(c)
    print keypad[cur[0]][cur[1]]
            
