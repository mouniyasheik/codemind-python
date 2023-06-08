def fun(n):
    
    for i in range(2,n//2+1):
        if n%i==0:
            return 0
    return 1
n1=int(input())
n11=int(input())
n2=n1+n11
for i in range(1,n2):
    if fun(i+n2)==1:
        print(i)
        break