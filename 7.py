a=str(input())
b=0
c=0
d=0
for i in range(len(a)):
 if a[i]=="+":
     b+=1
 if a[i]=="-":
     c+=1
 if (a[i]=="+" or a[i]=="-") and a[i+1]=="0":
     d+=1
print(b,' ',c,' ',d)
