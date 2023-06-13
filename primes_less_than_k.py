def fun(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return 0
    return 1
n=int(input())
s=0
c=0
a=list(map(int,input().split()))
b=int(input())
for i in a:
    
    if i<=b:
        if i==1:
            continue
        elif fun(i)==1:
            s=s+i
            c=c+1
print(c)