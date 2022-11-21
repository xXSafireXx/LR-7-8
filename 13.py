a=str(input())
b=0
for i in range(len(a)):
    if a[i]=='a' or a[i]=='b' or a[i]=='c':
     b=0
    else:
        b=1
        break
if b==0:
 print('yes')
else:
    print('no')
