n=int(input())
a=list(map(int,input().split()))
b=[]
s=0
for i in a:
    if i not in b:
        b.append(i)
        if i%2==0:
            
               s=s+i
print(s)