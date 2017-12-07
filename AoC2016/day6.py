with file("day6.txt",'r') as f:
    strings=f.readlines()

chars={0:dict(),1:dict(),2:dict(),3:dict(),4:dict(),5:dict(),6:dict(),7:dict()}
for line in strings:
    line=line.strip()
    for i in range(len(line)):
        if chars[i].get(line[i])==None:
            chars[i][line[i]]=1
        else:
            chars[i][line[i]]+=1
r=""
r2=""
for i in chars:
    r+=max(chars[i].items(),key=lambda t:t[1])[0]
    r2+=min(chars[i].items(),key=lambda t:t[1])[0]

print r,r2
