def chck_seq(seq):
    for i in range(len(seq)-1):
        if seq[i]==seq[i+1]:
            return False
    return True

cnt=0
while True:
    x=cnt+(14*182)
    seq=[]
    while True:
        if x==0:
            break
        seq.append(x%2)
        x/=2
    if chck_seq(seq):
        break
    cnt+=1
print seq,chck_seq(seq),cnt