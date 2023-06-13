n=int(input())
s=m=0
l=list(map(int,input().split()))
a,b=map(int,input().split())
for i  in  range(len(l)):
    if l[i]>=a and l[i]<=b:
        s=s+l[i]
print(s)