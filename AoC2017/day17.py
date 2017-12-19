inp=386

l=[0]
cur=0

"""
part1
"""
while True:
    val=l[cur]+1
    cur=(cur+inp)%len(l)+1
    l.insert(cur,val)
    if val==2017:
        print l[(cur+1)%len(l)]
        break

"""
part2
"""     
length=1
cur_i=0
cur_v=0
cur_v1=-1
while True:
    cur_v+=1
    cur_i=(cur_i+inp)%length+1
    if cur_i==1:cur_v1=cur_v
    length+=1
    if length==50000000:
        print cur_v1
        break
