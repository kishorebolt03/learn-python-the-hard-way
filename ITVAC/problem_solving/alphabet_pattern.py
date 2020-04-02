'''
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
'''

import math
n=int(input())
char=97
for i in range(n):
    if i < n :
        m=n
        s=''
        s1=''
        for j in range(i+1):
            s+=chr(char+m-1)
            m-=1
        s1=s+s[i::-1][1:] if (len(s)>1 or len(s)<n) else s
        print('--'*((n-len(s)))+'-'.join(s1)+'--'*(n-len(s)))
