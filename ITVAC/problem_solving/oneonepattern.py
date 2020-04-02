#oneonepattern

def oneone(n):
    i=0
    while i<n:

        print(11**(i+1))
        i+=1


n=int(input())
a=[]
for i in range(n):
    b=int(input())
    a.append(b)
    oneone(a[i])
    print("|||||")
