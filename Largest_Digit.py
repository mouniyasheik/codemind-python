n=int(input())
h=0
while n!=0:
    r=n%10
    if r>h:
        h=r
    n=n//10
print(h)