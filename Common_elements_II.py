n,m=list(map(int,input().split()))


a=list(map(int,input().split()))
b=list(map(int,input().split()))
d=[]
for i in a:
    if i not in b:
        if i not in d:
            d.append(i)
            
for i in b:
    if i not in a:
        if i not in d:
            d.append(i)
                   
print(*d)
