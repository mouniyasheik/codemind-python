n=int(input())
s=0
a=[]
l=list(map(int,input().split()))
b=int(input())
for i in l:
    if b==l.count(i):
        if i not in a:
            a.append(i)
            s=1
if s==1:
    for i in range(0,len(a)):
        
        print(a[i],end=" ")

else:
         print('-1')
