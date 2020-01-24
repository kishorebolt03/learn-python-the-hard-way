
def mindenom(a):
    n=a
    st=[500,100,50,20,10,5,2,1]
    sc=[0,0,0,0,0,0,0,0]
    f=0
    for i,j in zip(st,sc):
        if n>i:
            j=n//i
            n=n-j*i
            print(i,":",j)
        else:
            print(i,":",j)


n=int(input())
s=[]
for i in range(0,n):
    k=int(input())
    s.append(k)
    
for i in s:
    mindenom(i)
