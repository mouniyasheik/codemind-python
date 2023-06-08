n=int(input())
c=0
a=map(int,input().split())
nn=int(input())
for i in a:
    if i==nn:
        c+=1
if c==0:
    print("False")
else:
    print("True")