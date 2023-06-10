n=int(input())
s=x=0
a=list(map(int,input().split()))
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(*b)