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
