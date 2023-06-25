n=int(input())
c=0
b=[]
a=list(map(int,input().split()))
for i in a:
    x=a.count(i)
    if i not in b:
        b.append(i)
        c=c+(x//2)
print(c)