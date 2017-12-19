with file("day7.txt","r") as f:
    lines=[x.strip() for x in f.readlines()]

# lines=["pbga (66)",
# "xhth (57)",
# "ebii (61)",
# "havc (66)",
# "ktlj (57)",
# "fwft (72) -> ktlj, cntj, xhth",
# "qoyq (66)",
# "padx (45) -> pbga, havc, qoyq",
# "tknk (41) -> ugml, padx, fwft",
# "jptl (61)",
# "ugml (68) -> gyxo, ebii, jptl",
# "gyxo (61)",
# "cntj (57)"]


def check_weights(node):
    if not inp[node]["names"]:
        return 0
    vals=[]
    for i in inp[node]["names"]:
        tmp=check_weights(i)
        if isinstance(tmp,int):
            vals.append(tmp+inp[i]["weight"])
        else:
            vals.append(sum(tmp)+inp[i]["weight"])
    return vals

def find_root(d):
    for i in d:
        root=i
        for j in d:
            if root in d[j]["names"]:
                root=None
        if root!=None:
            return root

inp={}
for i in lines:
    split=i.split(" -> ")
    names=[]
    if len(split)>1:
        names=split[1].split(", ")
    split2=split[0].split(" ")
    inp[split2[0]]={"weight":int(split2[1].split("(")[1].split(")")[0]),"names":names}

"""
part1
"""
root=find_root(inp)
print root

"""
part2
"""
s=[]
while True:
    values=check_weights(root)
    s=list(set(values))
    if len(s)==1:
        s2=list(set(old_values))
        ind=old_values.index(s2[0]) if old_values.count(s2[0])<old_values.count(s2[1]) else old_values.index(s2[1])
        print inp[root]["weight"]-abs(old_values[old_values.index(s2[0])]-old_values[old_values.index(s2[1])]),root
        break
    else:
        old_values=list(values)
    index=values.index(s[0]) if values.count(s[0])<values.count(s[1]) else values.index(s[1])
    root=inp[root]["names"][index]



