from hashlib import md5
import re
inp="ahsbgdzn"
inp="abc"

def hashme(s,flag):
    h=md5(s).hexdigest()
    if flag:
        for i in range(2016):
            h=md5(h).hexdigest()
    return h

keys=set()
i=0
part2=True
while True:    
    hashed=hashme(inp+str(i),part2)
    res=re.search("(\w)\\1{2}",hashed)
    if res!=None:
        c=hashed[res.end()-1]
        for l in xrange(i+1,i+1001):
            h=hashme(inp+str(l),part2)
            if c*5 in h:
                keys.add(hashed)
                print i
                break
    if len(keys)==64:
        break
    i+=1

print i
    
    


