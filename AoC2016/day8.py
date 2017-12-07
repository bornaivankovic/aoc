from __future__ import print_function
import numpy
with file("day8.txt",'r') as f:
    strings=f.readlines()

display=[["." for x in range(50)] for y in range(6)]
def print_display():
    for i in display:
        for j in i:
            print(j,end="")
        print()

def parse_line(line):
    split=line.split(" ")
    if line.startswith("rect"):        
        rect=(int(split[1].split('x')[0]),int(split[1].split('x')[1]))
        for i in range(rect[0]):
            for j in range(rect[1]):
                display[j][i]='#'
    else:
        if split[1]=="row":
            y=int(split[2].split('=')[1])
            n=int(split[-1])
            display[y]=numpy.roll(display[y],n)
        else:
            x=int(split[2].split('=')[1])
            n=int(split[-1])
            col=[display[i][x] for i in range(6)]
            col=numpy.roll(col,n)
            for i in range(6):
                display[i][x]=col[i]


for line in strings:
    parse_line(line.strip())
print_display()
s=0
for i in range(6):
    for j in range(50):
        if display[i][j]=="#":
            s+=1
print(s)
