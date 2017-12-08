import operator
with file("day8.txt","r") as f:
    ins=[x.strip() for x in f.readlines()]

# ins=[
#     "b inc 5 if a > 1",
# "a inc 1 if b < 5",
# "c dec -10 if a >= 1",
# "c inc -20 if c == 10"
# ]
reg={}
m=0
for i,j in zip(ins,range(1,1+len(ins))):
    split=i.split(" if ")
    split2=split[1].split(" ")
    r=split2[0]
    if reg.get(r) is None: reg[r]=0
    if eval("reg[\""+r+"\"] "+"".join(split2[1:])):
        split2=split[0].split(" ")
        r=split2[0]
        if reg.get(r) is None: reg[r]=0
        inc=True if split2[1]=="inc" else False
        val=int(split2[2])
        if inc:
            reg[r]+=val
        else:
            reg[r]-=val
        if reg[r]>m: m=reg[r]

"""
part1
"""
print reg[max(reg.iteritems(), key=operator.itemgetter(1))[0]]
"""
part2
"""
print m