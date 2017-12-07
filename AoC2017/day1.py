with file("day1.txt","r") as f:
    line=f.readline().strip()

matched=[]

"""
part 1
"""
# for i in range(len(line)-1):
#     if line[i]==line[i+1]:
#         matched.append(line[i])
# if line[0]==line[-1]:
#     matched.append(line[-1])

"""
part 2
"""
half=len(line)/2
for i in range(len(line)):
    if i<half:
        if line[i]==line[i+half]:
            matched.append(line[i])
    else:
        if line[i]==line[-len(line)+(i-half)]:
            matched.append(line[i])

matched=[int(x) for x in matched]
print sum(matched)