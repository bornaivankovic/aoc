import re
with file("day9.txt","r") as f:
    line=f.readline().strip()

garbage_regex="<([^>]*)>"
escape_regex="!.{1}"
removed_garbage=0

def calc_score(line):
    depth=0
    score=0
    for i in line:
        if i=="{":
            depth+=1
            score+=depth
        elif i=="}":
            depth-=1
    return score

def remove_escaped(s):
    return re.sub(escape_regex,"",s)
    
def repl_comma(s):
    while True:
        m=re.search("(\{,\{)|(\},\})|(\{,\})",s)
        if m is None:
            break
        s=s[:m.start()+1]+s[m.end()-1:]
    return s

def count_garbage(matchobj):
    global removed_garbage
    removed_garbage+=len(matchobj.group())-2
    return ""

def remove_garbage(s):
    x=re.sub(",{2,}",",",re.sub(garbage_regex,count_garbage,s))
    return repl_comma(x)

line=remove_escaped(line)
line=remove_garbage(line)
print calc_score(line)
print removed_garbage
