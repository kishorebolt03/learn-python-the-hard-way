'''
* * * *
*       *
*       *
*       *
* * * *
*       *
*       *
*       *
* * * *
'''




n=int(input())
for i in range(n):
    for j in range(n-2):
        if ((i==0 or i==n-1 or i==n//2) and j<n-3 ) or j==0 or (j==n-3 and i>0 and i<n//2)or (j==n-3 and i>n//2 and i<n-1):
            print("*",end=' ')
        else:
            print(end='  ')
    print()


n=9
for i in range(n):
    if i==0 or i==n//2 or i==n-1:
        print("* "*(n-(n//2)-1))
    else:
        print("*"," "*(n-(n//2)),"*")
