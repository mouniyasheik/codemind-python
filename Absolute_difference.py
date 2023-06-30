def prime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return 1
    return 0
n=int(input())
l=list(map(int,input().split()))
s=1
e=1
for i in l:
        if prime(i)==1:
            s=s*i
        else:
            e=e*i
print(abs(s-e))