n=int(input())

a=map(int,input().split())
c=0
nn=int(input())
for i in a:
    if i==nn:
        c+=1
print(c)