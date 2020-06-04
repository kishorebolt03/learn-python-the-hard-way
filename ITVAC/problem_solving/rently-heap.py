import heapq
from math import ceil
n=int(input())
l=list(map(int,input().split()))
k=int(input())
len1=len(l)//2
for i in range(n+1):
    heapq.heapify(l)
    #print(l)
    #l=list(l)
    l.append(ceil(l.pop(len1)/2))
    #print(l)
print(sum(l))

