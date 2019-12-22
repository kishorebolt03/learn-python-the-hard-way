n=int(input())
k=n*2-1
for i in range((n*2)-1):
    for j in range((n*2)+1):
        if i==j or (j==(n*2)-2-i and (j!=i-1 or j!=i+1)):
            print("*",end=' ')
        else:
            print(end=' ')
    print()
