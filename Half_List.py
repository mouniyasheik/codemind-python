n=int(input())

d=[]
a=list(map(int,input().split()))
for i in range(n-1,n//2-1,-1):
    d.append(a[i])

for i in range(0,n//2):
    d.append(a[i])
print(*d)
    
    