n=int(input())
s=m=0
c=[]
l=list(map(int,input().split()))

for i  in  range(len(l)):
    if  l[i]%2==0:
        c.append(l[i])
        s=s+l[i]
    else:
        m+=1
        break
print(s)