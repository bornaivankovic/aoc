inp=29000000

def factors(n):    
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

"""
part1
"""
i=1
while True:
    pres=0
    for j in factors(i):
        pres+=10*j
    if pres>=inp:
        print i
        break
    i+=1

"""
part2
"""
i=1
while True:
    pres=0
    for j in factors(i):
        if i>50*j:
            continue
        pres+=11*j
    if pres>=inp:
        print i
        break
    i+=1

