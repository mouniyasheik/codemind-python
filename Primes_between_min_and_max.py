def fun(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return 0
    return 1
n=int(input())
c=0
a=list(map(int,input().split()))
m=a.index(max(a))
m1=a.index(min(a))
if m<m1:
    for i in range(m,m1):
    
        
        if fun(a[i])==1:
            c=c+1
else:
    for i in range(m1,m+1):
    
        
        if fun(a[i])==1:
            c=c+1
print(c)