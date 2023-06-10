n=int(input())
s=m=0
l=list(map(int,input().split()))
a,b=map(int,input().split())
for i  in  range(len(l)):
    if l[i]<a:
         s=s+l[i]
    elif l[i]  >b  :
        m=m+l[i]
print(s+m)
