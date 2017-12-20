from operator import add
from itertools import combinations
with file("day20.txt","r") as f:
    lines=[x.strip() for x in f.readlines()]

particles=[]
# lines=[
#     "p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>",
#     "p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>"
# ]
for line in lines:
    particles.append([eval("("+x.split("=")[1][1:-1]+")") for x in line.split(", ")])

def get_distances():
    return [sum(map(abs,x[0])) for x in particles]

def update():
    global particles
    for i in particles:
        i[1]=tuple(map(add,i[1],i[2]))
        i[0]=tuple(map(add,i[0],i[1]))

def remove_collisons():
    global particles
    rem=set()
    for i in combinations(particles,2):
        if i[0][0]==i[1][0]:
            rem.add(tuple(i[0]))
            rem.add(tuple(i[1]))
    for i in rem:
        particles.remove(list(i))
    return len(rem)



cnt=len(particles)
for i in range(10000):
    update()
    cnt-=remove_collisons()
    dist=get_distances()
    m=min(dist)
    if i%100==0:
        print dist.index(m),cnt