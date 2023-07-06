n=int(input())
for ii in range(n):
    s=int(input())
    l=list(map(int,input().split()))
    i=0
    j=s-1
    d=[]
    while i<=j:
        d.append(l[j])
        j-=1
        if l[i] not in d:
            d.append(l[i])
            i+=1
    print(*d)