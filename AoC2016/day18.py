with file("day18.txt",'r') as f:
    inp=f.read()

rows=[]
row_n=400000
rows.append(inp.strip())

def display():
    for i in rows:
        s=""
        for j in range(len(i)): s+=i[j]
        print s

def new_row(prev):
    row=rows[prev]
    nr=""
    for i in range(len(row)):
        if i==0: l="."
        else: l=row[i-1]
        if i==len(row)-1: r="."
        else: r=row[i+1]
        c=row[i]
        if l=="^" and c=="^" and r!="^": t="^"
        elif l!="^" and c=="^" and r=="^": t="^"
        elif l=="^" and c!="^" and r!="^": t="^"
        elif l!="^" and c!="^" and r=="^": t="^"
        else: t="."
        nr+=t
    return nr

for i in range(1,row_n):
    rows.append(new_row(i-1))


cnt=0
for i in rows:
    cnt+=i.count('.')

print cnt
