n=int(input())
s=m=0
c=[]
l=list(map(int,input().split()))
b=int(input())
for i  in  range(len(l)):
    if  l[i]<b or l[i]==b:
        c.append(l[i])
        s=s+l[i]
print(s)