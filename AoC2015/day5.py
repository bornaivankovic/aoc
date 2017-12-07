import re
with file("day5.txt",'r') as file:
    strings=file.readlines()
vowels=["a","e","i","o","u"]
nope=["ab","cd","pq","xy"]
asdf=["ugknbfddgicrmopn","aaa","jchzalrnumimnmhp","haegwjzuvuyypxyu","dvszwmarrgswjxmb"]
def check(s):
    flag1,flag2,flag3=False,False,True
    vow=0
    for v in vowels:
        for x in range(len(s)):
            if v==s[x]:
                vow+=1
    for i in range(len(s)-1):
        if(s[i]==s[i+1]):
            flag2=True
    for n in nope:        
        if re.search(n,s)!=None:
            flag3=False
    if vow>=3:
        flag1=True
    return flag1 and flag2 and flag3
i=0
for line in strings:
    if check(line):
        i+=1

print i