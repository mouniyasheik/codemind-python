def num(j):
    t=j
    s=0
    while(t>0):
        r=t%10
        s+=1
        t=t//10
    if s%2==0:
        return 1
    else:
        return 0
n=int(input())
s=list(map(int,input().split()))
c=0
for i in s:
        if num(i)==1:
            c+=1
print(c)