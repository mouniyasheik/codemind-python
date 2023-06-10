n=int(input())
s=m=0
l=list(map(int,input().split()))
for i in range(len(l)):
    if l[i]%2==0:
        print(l[i],end=" ")
for i in range(len(l)):
    if l[i]%2!=0:
        print(l[i],end=" ")
      