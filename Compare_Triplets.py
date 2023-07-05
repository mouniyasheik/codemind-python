l=list(map(int,input().split()))
a=list(map(int,input().split()))
s=b=0
for i in range(len(l)):
    if l[i]>a[i]:
        s+=1
    elif l[i]<a[i]:
        b+=1
print(s,b)