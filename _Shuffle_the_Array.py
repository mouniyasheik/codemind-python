n=int(input())
l=list(map(int,input().split()))
nn=int(input())
i=0
j=n//2
p=[]
while i<nn:
    p.append(l[i])
    i+=1
    if j<n:
        p.append(l[j])
        j+=1
print(*p)    
   