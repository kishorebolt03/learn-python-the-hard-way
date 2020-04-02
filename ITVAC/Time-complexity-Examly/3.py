# you are using python
import math
n=int(input())
s=999999999999999999999
i=1
s1=[]
while i<s and i<math.sqrt(n):
    if n%1==0:
        k=n//1 + n//(n//1)
        if k<s:
            s=k
    i+=1
print(s)
