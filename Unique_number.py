n = int(input())
s=str(n)
unique = [int(x) for x in set(str(n))]
if len(unique)==len(s):
   print("Unique Number")
else:
    print("Not Unique Number")