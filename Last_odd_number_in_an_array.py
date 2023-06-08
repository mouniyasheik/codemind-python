n=int(input())
a=map(int,input().split())
x=0
for i in a:
    if i%2!=0:
        x=i
print(x)