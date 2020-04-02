n=int(input())
k=n*3
l=1
for i in range(n):
    for j in range(n-i):
        print(l,end=' ')
        l+=1
        k-=1
    if i!=n-1:
        print()
for i in range(n+1):
    for j in range(i):
        print(l,end=' ')
        l+=1
        k+=1
    print()
