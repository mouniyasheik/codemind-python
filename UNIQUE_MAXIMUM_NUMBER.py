n=int(input())
l=list(map(int,input().split()))
d=[]
v=0
for i in l:
    if l.count(i)==1:
        v+=1
        d.append(i)
if v==0:
    print("-1")
else:
    
     print(max(d))
        