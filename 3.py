a=str(input())
b=len(a)
if b%2==1:
 print(a[0],',',a[-1],',',a[b//2])
else:
     print(a[0],',',a[-1])
