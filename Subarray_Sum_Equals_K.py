a,b=list(map(int,input().split()))
c=list(map(int,input().split()))
d=0

for i in range(0,a):
    s=0
    for j in range(i,a):
        s+=c[j]
        if s==b:
            d+=1
            break
print(d)
            
        
