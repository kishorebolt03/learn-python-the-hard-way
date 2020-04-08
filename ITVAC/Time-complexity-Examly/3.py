# you are using python
'''
You are given an integer N denoting whose factors are A and B. You have to find the minimum value of A+B for any integer A and B.

Value of N is

1<=N<=10^13
NOTE: long long int

'''
import math
n=int(input())
s=999999999999999999999
i=1
s1=[]
while i<s and i<math.sqrt(n):
    if n%i==0:
        k=n//i + n//(n//i)
        if k<s:
            s=k
    i+=1
print(s)
