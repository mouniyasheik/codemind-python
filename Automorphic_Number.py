n=int(input())
l=len(str(n))
sq=n**2
r=sq%pow(10,l)
sq/=10
if(r==n):
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')
