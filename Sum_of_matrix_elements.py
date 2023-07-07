n=int(input())
s=int(input())
o=0
for i in range(n):
    l=list(map(int,input().split()))
    o=o+sum(l)
print(o)