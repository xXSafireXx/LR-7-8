a=str(input())
b=''
if len(a)>10:
    for i in range(6):
        b+=a[i]
    print(b)
else:
    while len(a)!=12:
        a+='o'
    print(a)
        
