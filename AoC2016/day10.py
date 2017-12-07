with file("day10.txt",'r') as f:
    strings=f.readlines()

bots={}
instructions=[]
for line in strings:
    split=line.strip().split(" ")
    if line.startswith("value"):        
        if bots.get(int(split[-1]))==None:
            bots[int(split[-1])]=[int(split[1])]
        else:
            bots[int(split[-1])].append(int(split[1]))
    else:
        instructions.append({"bot":int(split[1]),"high":int(split[-1]),"low":int(split[6])})
flag=True
while flag:
    bot=filter(lambda x:len(bots[x])>=2,bots)
    if(len(bot)<1):
        flag=False
    for b in bot:
        ins=filter(lambda x:x["bot"]==b,instructions)[0]
        if ins==None:
            flag=False
        high=max(bots[b])
        low=min(bots[b])
        if 61 in bots[b] and 17 in bots[b]:
            print b
        if bots.get(ins["high"])== None:
            bots[ins["high"]]=[high]
        else:
            bots[ins["high"]].append(high)
        if bots.get(ins["low"])== None:
            bots[ins["low"]]=[low]
        else:
            bots[ins["low"]].append(low)
        bots.pop(b)

print bots

