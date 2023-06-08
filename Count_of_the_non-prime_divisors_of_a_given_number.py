def fun(n):
    
    for i in range(2,n//2+1):
        if n%i==0:
         return 0   
            
    return 1

n=int(input())
c=1
for i in range(1,n+1):
    if n%i==0:
        
         if fun(i)==0:
             
            c+=1
print(c)


