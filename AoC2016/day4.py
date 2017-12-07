with file("day4.txt",'r') as f:
    strings=f.readlines()

def get_checksum(d):
    vals=sorted(d.items(),key=lambda t: (t[1],t[0]),reverse=True)
    if len(vals)<5:
        return 0

    s=set()
    for i in vals:
        s.add(i[1])
    vals2=dict()
    for i in s:
        for j in vals:
            if j[1]==i:
                if vals2.get(i)==None:
                    vals2[i]=[j]
                else:
                    vals2[i].append(j)
    j=0
    r=""
    for i in reversed(vals2.keys()):
        for k in sorted(vals2[i],key=lambda t:t[0]):
            if j==5:
                return r
            r+=k[0]
            j+=1

def rotate(c,n):
    for i in range(n):
        if c=="z":
            c='a'
            continue
        c=chr(ord(c)+1)
    return c

s=0
for line in strings:
    split=line.strip().split("-")
    a=split[-1:][0]
    split=split[:-1]
    sector=int(a.split("[")[0])
    chcksum=a.split("[")[1][:-1]
    chars={}
    for i in split:
        for j in i:
            if chars.get(j)==None:
                chars[j]=1
            else:
                chars[j]+=1
    my_chcksum=get_checksum(chars)
    if my_chcksum== chcksum:
        s+=sector
        res=""
        for i in split:
            for j in i:
                res+=rotate(j,sector) 
            res+=" "   
        if "north" in res:
            print res, sector
print s