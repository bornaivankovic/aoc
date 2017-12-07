# import numpy
# import matplotlib.pyplot as plt
inp=3004953
inp=9

# t=[(1,i+1) for i in range(inp)]
# while max(t,key=lambda x:x[0])[0]!=inp:
#     t[0]=(t[0][0]+t[len(t)/2][0],t[0][1])
#     t.remove(t[len(t)/2])
#     t=[(i,j) for (i,j) in numpy.roll(t,-1,0)]
#     if len(t)%10000==0:
#         print len(t)

# print max(t,key=lambda x:x[0])
# removed=[]
# won=[]
# for inp in range(512):
#     rem=[]
#     t=[i+1 for i in range(inp)]
#     t2=t
#     while len(t)>1:
#         #t[0]=(t[0][0]+t[len(t)/2][0],t[0][1])
#         rem.append(t2.index(t[len(t)/2]))
#         t.remove(t[len(t)/2])              
#         t= numpy.roll(t,-1).tolist()
#     removed.append(rem)
#     if t:
#         won.append(t[0])
n=0
inp=3004953
while True:
    if inp>=(3**n)+1 and inp<=3**(n+1):
        if inp<=2*3**n:
            print inp-(3**n)
            break
        else:
            print 2*inp-3**(n+1)
            break
    n+=1
print n


# vals={}
# for i in removed:
#     for j in i:
#         if vals.get(j)==None: vals[j]=1
#         else: vals[j]+=1
# x=vals.keys()
# y=[vals[i] for i in x]

# x=range(1,512)
# y=won
# x_2=[i-27 for i in x]
# x_3=[2*i-81 for i in x]
# plt.plot(x,y,'ro',x,x_2,'bs',x,x_3,'g^')
# plt.grid(True)
# plt.show()

#print t