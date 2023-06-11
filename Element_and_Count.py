n=int(input())
s=[]
b=[]
a=list(map(int,input().split()))
for i in range(0,n):
    if a[i] not in b:
        


         b.append(a[i])
    
         x=a.count(a[i])
         s.append(x)
m=len(b)
for i in range(0,m):
    
    print(b[i],s[i],end=" ")