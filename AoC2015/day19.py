import re
with file("day19.txt","r") as f:
    lines=[x.strip() for x in f.readlines()]

molecule=lines[-1]
repl={}
for line in lines:
    split=line.split(" => ")
    if len(split)>1:
        repl[split[1]]=split[0]

molecules=set()
for i in repl.items():
    split=molecule.split(i[1])
    for j in range(1,len(split)):
        molecules.add(i[1].join(split[:j])+i[0]+i[1].join(split[j:]))

print len(molecules)


"""
reversing everything helps >.<
"""
molecule=molecule[::-1]
repl={}
for line in lines:
    split=line.split(" => ")
    if len(split)>1:
        repl[split[1][::-1]]=split[0][::-1]

def rep(x):
    return repl[x.group()]

cnt=0
while molecule != 'e':
    molecule = re.sub('|'.join(repl.keys()), rep, molecule, 1)
    cnt+=1

print cnt

            
