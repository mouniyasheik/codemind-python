n=int(input())
s=x=0
a=list(map(int,input().split()))

for i in a:
    if i!=0 and i!=1:
        print(False)
        break
else:
        print(True)
        
    