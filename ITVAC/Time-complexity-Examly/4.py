def find(arr,n):
    ge=[0]*n
    se=[0]*n
    ge[0]=arr[0]
    se[n-1]=arr[n-1]
    for x in range(1,n):
        ge[x]=max(ge[x-1],arr[x])
    for x in range(n-2,-1,-1):
        se[x]=min(se[x+1],arr[x])
    cnt=0
    #print(se,ge)
    for y in range(n-1):
        if se[y+1]>ge[y]:
            cnt+=1
    #print(cnt)
    if cnt%2==0:
        print('Ashish')
    else:
        print('Jeel')
t=int(input())
while t>0:
    n=int(input())
    arr=[int(a) for a in input().split()]
    find(arr,n)
    t-=1
