import math
import heapq
listForTree = [2]
heapq._heapify_max(listForTree)
#print(listForTree)
# heapq.heapify(listForTree)
# print(listForTree)

#print(listForTree)
i=0
while i<1:
    m=heapq._heappop_max(listForTree)/2
    heapq.heappush(listForTree,math.ceil(m))
    heapq._heapify_max(listForTree)
    #print("pass ",i+1,listForTree)
    i+=1
print(sum((listForTree)))
