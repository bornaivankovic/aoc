from multiprocessing import Process,Value,Queue
with file("day18.txt","r") as f:
    lines=[x.strip() for x in f.readlines()]

"""
part1
"""
reg={}
cur=0
last_snd=None
rcvd=False

while True:
    if cur>=len(lines) or cur<0: break
    ins=lines[cur].split(" ")
    if not reg.get(ins[1]):
        reg[ins[1]]=0
    if "snd" in ins:
        last_snd=reg[ins[1]]
    if "set" in ins:
        try:
            reg[ins[1]]=int(ins[2])
        except:
            reg[ins[1]]=reg[ins[2]]
    if "add" in ins:
        try:
            reg[ins[1]]+=int(ins[2])
        except:
            reg[ins[1]]+=reg[ins[2]]
    if "mul" in ins:
        try:
            reg[ins[1]]*=int(ins[2])
        except:
            reg[ins[1]]*=reg[ins[2]]
    if "mod" in ins:
        try:
            reg[ins[1]]%=int(ins[2])
        except:
            reg[ins[1]]%=reg[ins[2]]
    if "rcv" in ins and reg[ins[1]]!=0:
        if not rcvd:
            print last_snd
            break
    if "jgz" in ins and reg[ins[1]]>0:
        cur+=int(ins[2])
        continue
    cur+=1

"""
part2
"""
def work(p,snd_cnt,q0,q1):
    def val(x):
        try:
            return int(x)
        except:
            return reg[x]
    reg={}
    cur=0
    reg["p"]=p
    while 0<=cur<len(lines)-1:
        ins=lines[cur].split(" ")
        if not reg.get(ins[1]):
            reg[ins[1]]=0
        if "snd" in ins:
            if p==1:
                snd_cnt.value+=1
            q1.put(reg[ins[1]])
        if "set" in ins:
            reg[ins[1]]=val(ins[2])
        if "add" in ins:
            reg[ins[1]]+=val(ins[2])
        if "mul" in ins:
            reg[ins[1]]*=val(ins[2])
        if "mod" in ins:
                reg[ins[1]]%=val(ins[2])
        if "rcv" in ins:
            reg[ins[1]]=q0.get()
        if "jgz" in ins and val(ins[1])>0:
            cur+=val(ins[2])
            continue
        cur+=1

if __name__=="__main__":
    cnt=Value('i',0)
    q0,q1=Queue(),Queue()
    p1=Process(target=work,args=(0,cnt,q0,q1))
    p2=Process(target=work,args=(1,cnt,q1,q0))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print cnt.value
