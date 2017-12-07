with file("day16.txt",'r') as f:
    lines=f.readlines()

aunts=[]
aunt={"children": 3,
"cats": 7,
"samoyeds": 2,
"pomeranians": 3,
"akitas": 0,
"vizslas": 0,
"goldfish": 5,
"trees": 3,
"cars": 2,
"perfumes": 1}
for l in lines:
    split=l.strip().split(":",1)
    s="{"
    for i in split[1].split(","):
        tmp=i.strip().split(":")
        s+="\""+tmp[0]+"\""+":"+tmp[1]+","
    s=s[:-1]
    s+="}"
    aunts.append(eval(s))
aunts2=[]
for i in aunts:
    l=0
    for j in aunt.keys():
        if i.get(j)!=None and i[j]==aunt[j]:
            l+=1
    if l==len(i.keys()):
        aunts2.append(i)

print aunts2



    
    