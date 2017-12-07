from itertools import permutations
ing={"Sprinkles":{"capacity":5, "durability":-1, "flavor":0, "texture":0, "calories":5},
"PeanutButter":{"capacity":-1, "durability":3, "flavor":0, "texture":0, "calories":1},
"Frosting":{"capacity":0, "durability":-1, "flavor":4, "texture":0, "calories":6},
"Sugar":{"capacity":-1, "durability":0, "flavor":0, "texture":2, "calories":8}}


def partitionfunc(n,k,l=1):
    '''n is the integer to partition, k is the length of partitions, l is the min partition element size'''
    if k < 1:
        raise StopIteration
    if k == 1:
        if n >= l:
            yield (n,)
        raise StopIteration
    for i in range(l,n+1):
        for result in partitionfunc(n-i,k-1,i):
            yield (i,)+result

part=partitionfunc(100,4,0)
m=0
mi=(0,0,0,0)
tmp={}
a=[]
for i in part:
    for k in permutations(i):
        tmp["capacity"]=0
        tmp["durability"]=0
        tmp["flavor"]=0
        tmp["texture"]=0
        tmp["calories"]=0
        for j in range(len(ing)):
            tmp["capacity"]+=ing[ing.keys()[j]]["capacity"]*k[j]
            tmp["durability"]+=ing[ing.keys()[j]]["durability"]*k[j]
            tmp["flavor"]+=ing[ing.keys()[j]]["flavor"]*k[j]
            tmp["texture"]+=ing[ing.keys()[j]]["texture"]*k[j]
            tmp["calories"]+=ing[ing.keys()[j]]["calories"]*k[j]
        tmpm=1
        for j in tmp:
            if j=="calories":
                continue
            if tmp[j]>0 and tmp["calories"]==500:
                tmpm*=tmp[j]
            else:
                tmpm=0
        if tmpm>m:
            m=tmpm
            mi=k

print m,mi

