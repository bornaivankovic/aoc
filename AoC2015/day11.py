inp="vzbxxyzz"
import re

def increment(pos):
    global inp
    tmp=ord(inp[pos])+1
    if tmp>ord("z"):
        tmp=ord("a")
        increment(pos-1)
    char=chr(tmp)
    inp=inp[0:pos]+char+inp[pos+pos:len(inp)]

while True:        
    flag1,flag2,flag3=False,False,False
    increment(len(inp)-1)
    if "o" not in inp and "i" not in inp and "l" not in inp:
            flag2=True
    for i in range(len(inp)-2):
        if chr(ord(inp[i])+1)==chr(ord(inp[i+1])) and chr(ord(inp[i+1])+1)==chr(ord(inp[i+2])):
            flag1=True                
    if re.search(r"(\w)\1.*(\w)\2",inp) is not None:
        flag3=True    
    if flag1 and flag2 and flag3:
        break

print inp
    
                


