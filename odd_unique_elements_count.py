n=int(input())
c=0
b=[]
l=list(map(int,input().split()))

for i in l:
    if i%2!=0:
        if i not in b:
             b.append(i)
             
print(len(b))
            
