c=[]
d=[]
n=int(input())
l=list(map(int,input().split()))
for i in range(len(l)):
    if i%2==0:
        c.append(l[i])
    else:
        d.append(l[i])
s=sum(c)  
e=sum(d)
s=abs(s-e)
if s%4==0:
    print("X")
else:
    print("Y")