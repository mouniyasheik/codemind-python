n=int(input())
a=list(map(int,input().split()))
x=0
for i in range(len(a)):
    if a[i]%2==0:
        x=i
print(x)