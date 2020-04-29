n=int(input())
a=0
b=0
for i in range(n,0,-1):
    print("* "*(i),end=' ')
    print("  "*a,end=' ')
    a+=1
    print("  "*b,end=' ')
    b+=1
    print("* "*i,end=' ')
    print()
a=n-1
for i in range(n):
    print('* '*(i+1),end=" ")
    print("  "*a,end=' ')
    print("  "*a,end=' ')
    a-=1
    print("* "*(i+1),end=' ')
    print()

