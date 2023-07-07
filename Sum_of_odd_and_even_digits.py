n=int(input())
s=[]
p=[]
l=list(map(int,input().split()))
for i in range(len(l)):
    if i%2!=0:
        s.append(l[i])
    else:
        p.append(l[i])
w=sum(s)-sum(p)
if w==0:
    print("YES")
else:
    print("NO")
        