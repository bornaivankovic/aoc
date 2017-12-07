import re
with file("day5.txt",'r') as file:
    str=file.readlines()
asdf=["qjhvhtzxzqqjkmpb","xxyxx","uurcxstgmygtbstg","ieodomkazucvgmuy"]
i=0
for line in str:
    start=0
    stop=2
    inc=1
    flag1,flag2=False,False
    while stop<=len(line):        
        tmp=line[start:stop]
        split=re.split(tmp,line,1)
        if re.search(tmp,split[0])!=None or re.search(tmp,split[1])!=None:
            flag1=True
        start+=inc
        stop+=inc
    for x in range(2,len(line)-1):
        if line[x]==line[x-2] and line[x]!=line[x-1]:
            flag2=True
    if flag1 and flag2:
        i+=1
print i