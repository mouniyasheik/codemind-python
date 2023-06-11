n=int(input())
s=m=0
a=[]
l=list(map(int,input().split()))
for i in l:
    if i==l.count(i):
        if i not in a:
            a.append(i)
if a!=[]:
    print(*a)

else:
         print('-1')
