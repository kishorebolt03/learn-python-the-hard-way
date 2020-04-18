n=5

for i in range(n*2+1):
    l=[]
    z=65+i
    for j in range(n*2+1):
        if j <n-i-1 :
            l.append(' ')
        if j >=n-i and j <=n and i<n:
            l.append('*')
        if j==n+1:
            l.append(' ')
        if j>n and i<n and j<=n+i+1:
            l.append(chr(z))
            z+=1
        if i>=n:
            if j<=i-n-1 and j<n:
                l.append(' ')

            if j<n and j>=i-n:
                l.append(str(i-j))
            if j>n and i>=n and j<n+i+1 and i<n*2 and j<=+n*2-(i-n):
                l.append(str((j-n)*2-1+(i-n)*2))
                

    print("".join(l))
    
    
    
