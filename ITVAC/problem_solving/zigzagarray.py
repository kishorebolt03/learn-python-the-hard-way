n=int(input())
a=[int(input()) for i in range(n) ]
for i in range(1,n):
    j=i-1
    if i%2==0 and a[i]>a[j]:
        a[j],a[i]=a[i],a[j]
    elif i%2!=0 and a[j]>a[i]:
        a[i],a[j]=a[j],a[i]
        
print(a)
