import md5
import re
secret="iwrupvqb"
start=0
stop=100000
inc=100000
flag=True

while flag:
    for i in range(start,stop):
        hexdigest=md5.new(secret+str(i)).hexdigest()
        if re.match("^0{6}",hexdigest) !=None:
            print i
            flag=False
            break
    start+=inc
    stop+=inc
