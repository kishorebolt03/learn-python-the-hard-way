


def splitt(s):
    x,y=s.split()
    x=list(x)
    y=list(y)
    if(x==y):
        print("strings are equal")
    else:
        print("strings are not equal")


N = int(input())
s=[]
for i in range(0,N):
    str1=input()
    s.append(str1)
for i in s:
    splitt(i)
