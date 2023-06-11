n=int(input())
c=0
b=[]
a=list(map(int,input().split()))
m=n//2+1
if n%2!=0:
    
    print(*a,'0')
else:
    
    print(*a)