n=int(input())
a=input()
for i in range(n):
    for j in range(1,n+i+1):
        if j<n-i:
            print(end=' ')
        else:
            print(a,end="")
    print()
k=1
f=1
for i in range(1,n):
    for j in range(1,k+i):
        print(end=' ')
    k+1
    while f<=(2*(n-i)-1):
        print(a,end='')
        f+=1
    f=1
    print()
