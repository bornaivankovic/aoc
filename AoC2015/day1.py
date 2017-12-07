with file("day1.txt",'r') as file:
    strings=file.readlines()[0]
plus='('
minus=')'
i=0
for a in range(1,len(strings)+1):
    if strings[a-1]==plus:
        i+=1
    if strings[a-1]==minus:
        i-=1
    if i==-1:
        print a
print i