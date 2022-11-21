a=str(input())
if a[0]=='a' and a[1]=='b' and a[2]=='c':
    del a(0,2)
    a[0]='w'
    a[1]='w'
    a[2]='w'
else:
    a+='zzz'
print(a)
