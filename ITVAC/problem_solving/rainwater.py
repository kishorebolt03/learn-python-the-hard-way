l=[3,2,1,0,3,2,0,2,1,0,1]
n=len(l)
w=0
t,r=[0 for i in range(n+1)],[0 for i in range(n+1)]
t[0]=l[0]
r[n-1]=l[n-1]
for i in range(1,n):
    t[i]=(max(t[i-1],l[i]))
for i in range(n-2,-1,-1):
    r[i]=(max(r[i+1],l[i]))
for i in range(0,n):
    w+=min(t[i],r[i])-l[i]
print(w)
