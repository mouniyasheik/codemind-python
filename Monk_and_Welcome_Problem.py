n=int(input())
l=list(map(int,input().split()))
p=list(map(int,input().split()))
i=0
j=0
while i<n and j<n:
    s=l[i]+p[j]
    print(s,end=" ")
    i+=1
    j+=1