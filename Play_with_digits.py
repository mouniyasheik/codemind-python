n=int(input())
s=0
a=list(map(int,input().split()))
for i in a:
    
    q=i
    while q!=0:
        r=q%10
        s=s+r
        q//=10
    
print(s)