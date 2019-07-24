n=int(input())
a=[]
c=0
d=0
for i in range(n+1):
    if d<n and i>0:
        b=int(input())
        a.append(b)
        d+=1
    c+=i

summ=sum(a)
diff=summ-c
m=max(a)
#print("summ ",summ)
#print("diff ",diff)
#print("c ",c)
print("missing num",m-diff)
