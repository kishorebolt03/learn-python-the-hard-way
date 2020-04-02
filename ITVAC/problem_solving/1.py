'''
for i in range(4):
    for j in range(4-i):
        print("# ",end="")
    print()
'''
'''
row=6
k=0
d=1
for i in range(6):
    k=1
    sps=" "
    for j in range(6-i):
        print(k,end="")
        k+=1
    print(" "*(i+2),end="")
    for j in range(6-i):
        print(6-i,end="")
    print()
    d=i*3
'''
n=7
m=13 
for row in range(1,n+1):
    for col in range(1,m+1):
        if  row == n or  row + col == n+1 or col-row == n-1:
            print("*",end="")
        else:
            print(end=" ")
    print()
