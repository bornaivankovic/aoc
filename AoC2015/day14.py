with file("day14.txt", 'r') as file:
    strings = file.readlines()

x=2503

reindeers=[]
for line in strings:
    split=line.strip().split(" ")
    reindeers.append({"name":split[0],"speed":int(split[3]),"time":int(split[6]),"rest":int(split[-2]),"dist":0,"resting":0,"running":0,"points":0})

def add_points(l):
    max_d=max(l,key=lambda x:x[1])[1]
    for i in reindeers:
        if i["dist"]==max_d:
            i["points"]+=1

for i in range(x):
    for j in reindeers:
        if j["running"]<=j["time"] and j["resting"]==0:
            j["dist"]+=j["speed"]
            j["running"]+=1
        else:
            j["resting"]-=1
        if j["running"]==j["time"]:
            j["resting"]=j["rest"]
            j["running"]=0
    asdf=[]
    for r in reindeers:
        asdf.append((r["name"],r["dist"]))
    add_points(asdf)

for r in reindeers:
        print (r["name"],r["points"])  



