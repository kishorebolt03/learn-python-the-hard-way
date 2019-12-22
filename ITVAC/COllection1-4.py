from collections import OrderedDict
from collections import Counter as C

d={}
d=OrderedDict()
n=int(input())
l=[]
for i in range(n):
    l.append(input())
d=C(l)
d={k:v for k,v in sorted(d.items(),key=lambda x:x[1], reverse=True)}
print(len(d))
for i in d.values():
    print(i,end=' ')
