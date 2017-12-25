with file("day25.txt","r") as f:
    lines=[x.strip() for x in f.readlines()]

start=lines[0][-2]
steps=int(lines[1].split()[-2])
rules={}
for i in range(3,len(lines),10):
    rules[lines[i][-2]]={
        "cur_0":{"write":int(lines[i+2][-2]),"move":lines[i+3].split()[-1][0],"next":lines[i+4][-2]},
        "cur_1":{"write":int(lines[i+6][-2]),"move":lines[i+7].split()[-1][0],"next":lines[i+8][-2]}
    }

tape=[0]
cur=0
cur_s=start
for i in xrange(steps):
    r=rules[cur_s]["cur_"+str(tape[cur])]
    tape[cur]=r["write"]
    cur=cur+1 if r["move"]=="r" else cur-1
    cur_s=r["next"]
    if cur==-1:
        tape.insert(0,0)
        cur=0
    elif cur==len(tape):
        tape.append(0)

print tape.count(1)
