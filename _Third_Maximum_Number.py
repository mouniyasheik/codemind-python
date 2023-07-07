n=int(input())
l=list(map(int,input().split()))
s=set(l)
p=[]
for  i in l:
    if i not in p:
        p.append(i)
p.sort()
if len(s)>=3:
    print(p[-3])
elif len(l)<3:
    print(max(l))
   