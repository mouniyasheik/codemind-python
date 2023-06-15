n=input()
c=[]
a=list(map(int,input().split()))
for i in a:
    s=0
    q=i
    while q!=0:
        r=q%10
        s=s*10+r
        q//=10
    c.append(s)
print(*c)