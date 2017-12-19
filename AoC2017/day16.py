from itertools import cycle
with file("day16.txt","r") as f:
    line=f.readline().strip()

progs="abcdefghijklmnop"
# progs="abcde"
# line="s1,x3/4,pe/b"
def dance():
    global progs
    for i in line.split(","):
        if "s" in i:
            progs=progs[-int(i[1:]):]+progs[:-int(i[1:])]
        elif "x" in i:
            swap_ind=[int(x) for x in i[1:].split("/")]
            swap_ind=sorted(swap_ind)
            progs=progs[:swap_ind[0]]+progs[swap_ind[1]]+progs[swap_ind[0]+1:swap_ind[1]]+progs[swap_ind[0]]+progs[swap_ind[1]+1:]
        elif "p" in i:
            swap_chars=i[1:].split("/")
            swap_chars=[progs.index(x) for x in swap_chars]
            swap_chars=sorted(swap_chars)
            progs=progs[:swap_chars[0]]+progs[swap_chars[1]]+progs[swap_chars[0]+1:swap_chars[1]]+progs[swap_chars[0]]+progs[swap_chars[1]+1:]

"""
part1
"""
dance()
print progs


"""
part2
through analysis of 1000 dances we can notice that for given input there are 48 unique ways programs can end up after dancing,
meaning the order programs end up after every 48 dances is the same
1000000000%48=16
so we have to do only 15 more to get to the state it would be after doing the requested 1000000000
"""
for i in xrange(15):
    dance()

print progs
