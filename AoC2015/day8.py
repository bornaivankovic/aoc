import re
with file("day8.txt",'r') as file:
    strings=file.readlines()

asdf=["\"\"","\"abc\"","\"aaa\\\"aaa\"","\"\\x27\""]

def parse(string):
    count=0
    a="\\\\\""    
    res=re.finditer(r"""(\\x[0-9a-f]{2})""",string)
    res2=re.finditer(r"""(\\\\)""",string)
    res3=re.finditer(r"""(\\\")""",string)
    count=len(string)+2
    if string[-3:len(string)]==a:
        count+=1
    for i in res:
        count+=3
    for i in res2:
        count+=1
    for i in res3:
        count+=1
    return count


chars_c=0
chars_m=0
for line in strings:
    x1=len(line.strip())
    y1=parse(line.strip())
    x2=len(line[:-1])
    y2=len(eval(line))
    chars_c+=x1
    chars_m+=y1

print chars_m-chars_c
print sum(2+s.count('\\')+s.count('"') for s in open('day8.txt'))
