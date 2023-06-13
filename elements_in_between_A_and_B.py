n=int(input())
s=m=0
c=[]
l=list(map(int,input().split()))
a,b=map(int,input().split())
for i  in  range(len(l)):
    if l[i]>=a and l[i]<=b:
        c.append(l[i])
        s=s+1
if s==0:
    print('-1')
else:
    
      print(*c)