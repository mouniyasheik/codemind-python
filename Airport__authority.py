n=int(input())
a=[]
for i in range(n):
    j=int(input())
    a.append(j)
s=int(input())
q=0
for i in range(n):
    if a[i]<=s:
        q+=1
    else:
        q+=2
print(q)