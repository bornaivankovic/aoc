with file("day15.txt","r") as f:
    lines=[x.strip() for x in f.readlines()]

facA=16807
facB=48271
div=2147483647

startA=int(lines[0].split(" ")[-1])
startB=int(lines[1].split(" ")[-1])
def part1():
    nexA=0
    nexB=0
    cnt=0
    for i in xrange(40000000):
        nexA=(startA*facA)%div if i==0 else (nexA*facA)%div
        nexB=(startB*facB)%div if i==0 else (nexB*facB)%div
        mask=1
        for j in xrange(17):
            if nexA&mask!=nexB&mask:
                break
            mask<<=1
        if j==16: cnt+=1
        
    return cnt

def part2():
    nexA=(startA*facA)%div 
    nexB=(startB*facB)%div
    cnt=0
    judgeA=[]
    judgeB=[]
    while len(judgeA)<5000000 or len(judgeB)<5000000:
        if nexA%4==0:
            judgeA.append(nexA)
        if nexB%8==0:
            judgeB.append(nexB)
        nexA=(nexA*facA)%div
        nexB=(nexB*facB)%div

    for (i,j) in zip(judgeA,judgeB):
        mask=1
        for k in xrange(17):
            if i&mask!=j&mask:
                break
            mask<<=1
        if k==16: cnt+=1
    return cnt

def main():
    print part1()
    print part2()

if __name__=="__main__":
    main()