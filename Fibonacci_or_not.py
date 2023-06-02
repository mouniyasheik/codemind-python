n=int(input())
a=0
k=0
b=1
for i in range(n):
    c=a+b
    a=b
    b=c
    
    if c==n:
        print(True)
        k+=1
if k==0:
    print("False")
