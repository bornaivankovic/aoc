with file("day3.txt",'r') as file:
    strings=file.readlines()[0]

visited={}
x1=0
y1=0
x2=0
y2=0

def coord(a):
    if a==0:
        return "{},{}".format(x1,y1)
    else:
        return "{},{}".format(x2,y2)

def inc(sign,flag):
    global x1,x2,y1,y2
    if flag==0:
        if sign=='<':
            x1-=1
        if sign=='>':
            x1+=1
        if sign=='v':
            y1-=1
        if sign=='^':
            y1+=1
    else:
        if sign=='<':
            x2-=1
        if sign=='>':
            x2+=1
        if sign=='v':
            y2-=1
        if sign=='^':
            y2+=1

visited[coord(0)]=2
for i in range(len(strings)):
    inc(str[i],i%2)
    if visited.get(coord(i%2))==None:
        visited[coord(i%2)]=1
    else:
        visited[coord(i%2)]+=1
print len(visited.keys())

