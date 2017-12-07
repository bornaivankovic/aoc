with file("day5.txt","r") as f:
    lines=f.readlines()

"""
part1
"""
instructions=[int(x.strip()) for x in lines]
cur=0
cnt=0
while True:
    try:
        next_cur=instructions[cur]
        instructions[cur]+=1
        cur+=next_cur
        cnt+=1
    except:
        print cnt
        break

"""
part2
"""
instructions=[int(x.strip()) for x in lines]
cur=0
cnt=0
while True:
    try:
        next_cur=instructions[cur]
        if next_cur>=3:
            instructions[cur]-=1
        else:
            instructions[cur]+=1
        cur+=next_cur
        cnt+=1
    except:
        print cnt
        break