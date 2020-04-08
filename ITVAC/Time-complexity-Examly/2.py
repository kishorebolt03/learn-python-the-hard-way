'''
You are going from City A to City B. The distance between A and B is S km. In the most days, you can go at most X  km one day. But there are N

 exceptions, in the Tith day, you can go at most Yi km. You need to find out the minimum number of days required to reach city B from city A

. 

Input Format
First line contains three integers, S,X,N(1≤S,X≤109,0≤N≤103)

.

The (i+1)

 th line contains two integers Ti,Yi(1≤Ti,Yi≤109)

.

It's guaranteed any two Ti  are different. Note that Ti is not sorted.



It is a time complexity based question. So need an efficient algorithm. Time limit is 1 second

Input Format
First line contains three integers, S,X,N(1≤S,X≤109,0≤N≤103)

.

The (i+1)

 th line contains two integers Ti,Yi(1≤Ti,Yi≤109)

.

It's guaranteed any two Ti are different. Note that Ti is not sorted.



Explanation for the sample test case below

In the first day, you walked 5 km.

In the second day, you walked 4 km.

In the third day, you walked 5 km.

In the fourth day, you walked 7 km and arrived.

'''

s, x, n = map(int, input().split())
days = 0
tra = 0
d = dict()
l = list()

for _ in range(n):
    a, b = map(int, input().split())
    d[a] = b
    l.append(a)
l.sort()
if l[0] == 1:
    tra = tra + d[l[0]]
    days = 1

else:
    tra = tra + (l[0] - 1) * x + d[l[0]]
    days = l[0]
for i in range(1,n):
    r = (l[i ] - l[i-1] - 1) * x
    if tra + r > s:
        break
    else:
        tra = tra + r+ d[l[i]]
        days = l[i]
    #print(i)
if tra <= s:
    e=(s-tra)
    if e%x==0:
        days=days+e//x
    else:
        days=days+1+e//x

print(days)
