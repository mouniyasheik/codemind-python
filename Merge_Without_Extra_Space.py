n=int(input())
for i in range(1,n+1):
    l,v=map(int,input().split())
    s=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a=[]
    for i in s:
             a.append(i)
    for i in b:
             a.append(i)
           
    a.sort()

    print(*a)
