n=int(input())
s=m=0
a=[]
l=list(map(int,input().split()))
for i in l:
    if i==l.count(i):
        if i not in a:
            a.append(i)
            s=s+i
if s>0:
    t=s/len(a)
    print(format(t,".2f"))
else:
    print('-1')
