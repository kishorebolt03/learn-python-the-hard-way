
def pattern(n):
    pat=1
    for i in range(n+1):
        for j in range(i):
            print(pat," ",end='')
            pat+=1
        print()






n=int(input())
s=[]
for i in range(0,n):
    k=int(input())
    s.append(k)

for i in s:
    pattern(i)
