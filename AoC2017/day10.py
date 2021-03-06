from itertools import cycle
with file("day10.txt","r") as f:
    line=f.readline().strip()
    lengths=[int(x) for x in line.split(",")]
    chars=[ord(x) for x in line]
    
l=[x for x in range(256)]
skip_size=0
cur=0

def rnd(lis):
    global cur,skip_size
    for i in lis:
        x=cycle(l)
        for j in range(cur):x.next()
        sub_l1=[x.next() for j in range(i)]
        sub_l1=sub_l1[::-1]
        cnt=0
        for j in sub_l1:
            l[(cur+cnt)%len(l)]=j
            cnt+=1
        cur+=i+skip_size
        cur%=len(l)
        skip_size+=1


def knot_hash(chars):
    chars+=[17, 31, 73, 47, 23]
    global l,skip_size,cur
    skip_size=0
    cur=0
    l=[x for x in range(256)]
    for i in range(64):
        rnd(chars)

    dense=[]
    for i in range(16):
        a=l[0+i*16:16+i*16]
        x=0
        for j in a:
            x^=j
        dense.append(x)
    s=""
    for i in dense:
        c=chr(i)
        s+=c
    return s.encode('hex')



def main():
    """
    part1
    """
    rnd(lengths)
    print l[0]*l[1]
    """
    part2
    """
    print knot_hash(chars)

if __name__=='__main__':
    main()
