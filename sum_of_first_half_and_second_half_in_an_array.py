n=int(input())
s=m=0
c=[]
l=list(map(int,input().split()))
a=n//2
for i  in  range(0,a):
    c.append(l[i])
    s=s+l[i]
for i in range(a,n):
    c.append(l[i])
    m=m+l[i]
print(s)
print(m)