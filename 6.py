a=str(input())
b=str(input())
if len(a)>len(b):
    for i in range(len(a)-len(b)):
        print(a)
else:
    for i in range(len(b)-len(a)):
        print(b)
