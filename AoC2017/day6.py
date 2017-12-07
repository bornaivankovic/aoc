with file("day6.txt","r") as f:
    lines=[x.strip() for x in f.readlines()]

# lines=["0\t2\t7\t0"]
banks=[int(x) for x in lines[0].split("\t")]

def redistribute(array,index):
    val=array[index]
    array[index]=0
    for i in range(1,val+1):
        array[(index+i)%len(array)]+=1
cnt=0
history=[]
while True:
    cnt+=1
    cur=banks.index(max(banks))
    tmp_banks=list(banks)
    history.append(tmp_banks)
    redistribute(banks,cur)
    if banks in history:
        print cnt
        print cnt - history.index(banks)
        break
    
