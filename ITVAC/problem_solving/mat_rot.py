def rotate(a,m,n,r,p):
    x = []
    for i in range(p,m-p-1): x.append(a[i][p])
    for j in range(p,n-p): x.append(a[m-p-1][j])
    for i in range(m-p-2,p,-1): x.append(a[i][n-p-1])
    for j in range(n-p-1,p,-1): x.append(a[p][j])
    cnt = len(x)
    r = cnt - (r % cnt)
    y = x[r:] + x[:r]
    k = 0
    for i in range(p,m-p-1): a[i][p] = y[k]; k+=1
    for j in range(p,n-p):   a[m-p-1][j] = y[k]; k+=1
    for i in range(m-p-2,p,-1): a[i][n-p-1] = y[k]; k+=1
    for j in range(n-p-1,p,-1): a[p][j] = y[k]; k+=1
    return

m,n,r = [int(i) for i in input().split(" ")]
d = min(m,n) //2
a=[]
for k in range(m):
    a.append([int(i) for i in input().split(" ")])

for p in range(d):
    rotate(a,m,n,r,p)

for k in range(m):
    print(' '.join(map(str,a[k])))
