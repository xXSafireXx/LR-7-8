a=str(input())
b=str(input())
c=len(a)
d=len(b)
if c>d:
    for i in range(c-d):
       print(a)
else:
    for i in range(d-c):
        print(b)
