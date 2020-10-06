#!/usr/bin/python3
n=int(input())
l=n*2-1
for i in range(l):
    for j in range(l):
        a=min( i , j , l-j-1 , l-i-1 )
        if (n-a)%2 == 0: print('0',end=' ')
        else:print('x',end=' ')
    print()
