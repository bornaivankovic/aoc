inp="3113322113"
#inp="1"

for x in range(50):
    inp2=""
    cur=inp[0]
    i=0
    while True:
        if i== len(inp):
            break
        if inp[i]!=cur:
            cur=inp[i]
        k=1
        while True:
            if i+k<len(inp): 
                if inp[i+k]==cur:
                    k+=1
                else:
                    break
            else:
                break
        inp2+=str(k)+cur
        i+=k
    inp=inp2

print len(inp)
        