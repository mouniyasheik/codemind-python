n,m=list(map(int,input().split()))
c=0
f=0
a=list(map(int,input().split()))
b=list(map(int,input().split()))
d=[]
for i in a:
    if i  in b:
        if i not in d:
            d.append(i)
            c+=1
for i in b:
    if i  in a:
        if i not in d:
            d.append(i)
            f+=1        
print(c+f)
