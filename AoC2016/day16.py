inp="10010000000110000"
disk_len=35651584
# inp="10000"
# disk_len=20

tmp=inp
while len(tmp)<disk_len:
    a=tmp
    b=""
    for i in range(-1,-len(a)-1,-1):
        b+=str(int(a[i])^1)
    tmp=a+"0"+b

tmp=tmp[:disk_len]
chcksum=""
while True:
    if len(tmp)%2==1:
        break
    chcksum=""
    for i in range(0,len(tmp)-1,2):
        if tmp[i]==tmp[i+1]:
            chcksum+="1"
        else:
            chcksum+="0"
    tmp=chcksum

print tmp

