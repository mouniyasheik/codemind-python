n,m=list(map(int,input().split()))
s=0
d=[]
a=list(map(int,input().split()))
for i in range(0,n):
    if a[i]%m!=0:
        d.append(i)
        s=s+1
print(s)
