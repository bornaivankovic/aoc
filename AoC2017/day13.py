with file("day13.txt","r") as f:
	lines=[x.strip() for x in f.readlines()]
	
# lines=["0: 3","1: 2","4: 4","6: 4"]

def calc_pos(cur,m,inc,n):
    if n==0:
        return cur,inc
    if inc>0:
        tmp=m-cur-1 if n+cur>m-1 else n
        cur+=tmp
        if cur==m-1:
            inc*=-1
        return calc_pos(cur,m,inc,n-tmp)
    else:
        tmp=cur if cur<=n else n
        cur-=tmp
        if cur==0:
            inc*=-1
        return calc_pos(cur,m,inc,n-tmp)

def move_sec(n=1):
    for i in firewall:
        step=n%(2*firewall[i]["max"]-2)
        cur,inc=calc_pos(firewall[i]["cur"],firewall[i]["max"],firewall[i]["inc"],step)
        firewall[i]["cur"],firewall[i]["inc"]=cur,inc

firewall={}
def init_firewall():
    for line in lines:
        split=line.split(": ")
        firewall[int(split[0])]={"cur":0,"max":int(split[1]),"inc":1}

def check_caught():
    for i in range(max(firewall.keys())+1):
        if firewall.get(i):
            if firewall[i]["cur"]==0:
                return True
        move_sec()
    return False
"""
par1
"""
total=0
init_firewall()
for i in range(max(firewall.keys())+1):
    if firewall.get(i):
        if firewall[i]["cur"]==0:
            total+=i*firewall[i]["max"]
    move_sec()

print total

"""
unoptimized pos
part2
"""
cnt=0
init_firewall()
while True:
    if cnt%10000==0:
        print cnt
    cnt+=1
    init_firewall()
    move_sec(cnt)
    if not check_caught():
        break

print cnt
