with file("day2.txt",'r') as file:
    strings=file.readlines()
res=0
for line in strings:
    l=int(line.split('x')[0])
    w=int(line.split('x')[1])
    h=int(line.split('x')[2])
    tmp=[l,w,h]
    tmp.remove(max(tmp))
    m=2*tmp[0]+2*tmp[1]
    a=l*w*h+m
    res+=a
print res
