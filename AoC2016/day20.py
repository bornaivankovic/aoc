with file("day20.txt",'r') as f:
    strings=f.readlines()

def test_ip(n):
    for start, end in ranges:
        if start <= n <= end:
            break
    else:
        if n < 2**32:
            return True
    return False

#strings=["5-8","0-2","4-7"]
ranges=[]
for line in strings:
    split=line.strip().split("-")
    ranges.append([int(split[0]),int(split[1])])

ranges=sorted(ranges,key=lambda x:x[0])
candidates = [x[1]+1 for x in ranges]

valids = [c for c in candidates if test_ip(c)]

total = 0
for ip in valids:
    while test_ip(ip):
        total += 1
        ip += 1

print(valids[0])
print(total)