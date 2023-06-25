n=int(input())
a=list(map(int,input().split()))
d=[]
c=0
for i in a:
    x=a.count(i)
    if x==1:
        d.append(i)
        c+=1
if c>0: 
    print(*d)
else:
        print('-1')
