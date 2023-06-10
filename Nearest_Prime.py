def fun(n):
    
    for i in range(2,n//2+1):
        if n%i==0:
            return 0
    return 1
n=int(input())
for i in range(1,n+1):
    a=int(input())
    for j in range(a,2*a+1):
        if fun(j)==1:
            x=j
            break
    for k in range(a,1,-1):
        if fun(k)==1:
            
            y=k
            break    
    if abs(a-x) == abs(a-y) :
         print(y)
    elif abs(a-x)> abs(a-y) : 
          print(y)
    else:
         print(x)