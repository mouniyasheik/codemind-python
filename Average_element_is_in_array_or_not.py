n=int(input())
k=0
a=list(map(int,input().split()))
c=sum(a)//len(a)
for i in a:
    if c==i:
        k+=1
if k==0:
    print("False")
else:
    print("True")