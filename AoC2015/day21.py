from itertools import combinations
with file("day21.txt","r") as f:
    lines=[x.strip() for x in f.readlines()]

shop={
    "Weapons":[{"Cost":8,"Damage":4,"Armor":0},{"Cost":10,"Damage":5,"Armor":0},{"Cost":25,"Damage":6,"Armor":0},{"Cost":40,"Damage":7,"Armor":0},{"Cost":74,"Damage":8,"Armor":0}],
    "Armor":[{"Cost":13,"Damage":0,"Armor":1},{"Cost":31,"Damage":0,"Armor":2},{"Cost":53,"Damage":0,"Armor":3},{"Cost":75,"Damage":0,"Armor":4},{"Cost":102,"Damage":0,"Armor":5}],
    "Rings":[{"Cost":25,"Damage":1,"Armor":0},{"Cost":50,"Damage":2,"Armor":0},{"Cost":100,"Damage":3,"Armor":0},{"Cost":20,"Damage":0,"Armor":1},{"Cost":40,"Damage":0,"Armor":2},{"Cost":80,"Damage":0,"Armor":3}]
}

def check_success(player,boss):
    player["Hit Points"],boss["Hit Points"]=100,109
    while True:
        boss_hit=1 if boss["Damage"]-player["Armor"]<1 else boss["Damage"]-player["Armor"]
        player_hit=1 if player["Damage"]-boss["Armor"]<1 else player["Damage"]-boss["Armor"]
        boss["Hit Points"]-=player_hit
        if boss["Hit Points"]<=0:
            return True
        player["Hit Points"]-=boss_hit
        if player["Hit Points"]<=0:
            return False

boss={}
for line in lines:
    split=line.split(": ")
    boss[split[0]]=int(split[1])

players=[]
for i in shop["Weapons"]:
    for j in shop["Armor"]+[None]:
        for k in list(combinations(shop["Rings"],0))+list(combinations(shop["Rings"],1))+list(combinations(shop["Rings"],2)):
            player={}
            cost=0
            dmg=0
            dmg+=i["Damage"]
            cost+=i["Cost"]
            arm=0
            if j:
                arm+=j["Armor"]
                cost+=j["Cost"]
            for l in k:
                if l:
                    dmg+=l["Damage"]
                    arm+=l["Armor"]
                    cost+=l["Cost"]
            player["Damage"]=dmg
            player["Armor"]=arm
            player["Cost"]=cost
            players.append(player)

success=[]
for i in players:
    if check_success(i,boss):
        success.append(i)

print min([x["Cost"] for x in success])

fail=[]
for i in players:
    if not check_success(i,boss):
        fail.append(i)

print max([x["Cost"] for x in fail])