n=int(input())
l=list(map(int,input().split()))
d=[]
for i in range(0,n,2):
    x=l[i]
    y=l[i+1]
    for i in range(1,y+1):
        d.append(x)
print(*d)