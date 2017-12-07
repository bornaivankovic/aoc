inp=3004953
# inp=5

t=[(1,i+1) for i in range(inp)]

while max(t,key=lambda x:x[0])[0]!=inp:
    if len(t)%2==0:
        for i in range(len(t)):
            if i%2==1:
                t[i]=(0,t[i][1])
            else:
                t[i]=(t[i][0]+t[i+1][0],t[i][1])
        
    else:
        for i in range(len(t)):
            if i%2==1:
                t[i]=(0,t[i][1])
            elif i%2==0 and i==len(t)-1:
                t[i]=(t[i][0]+t[0][0],t[i][1])
                t[0]=(0,t[0][1])
            else:
                t[i]=(t[i][0]+t[i+1][0],t[i][1])
    t=filter(lambda x:x[0]!=0,t)
    
        

print max(t,key=lambda x:x[0])
