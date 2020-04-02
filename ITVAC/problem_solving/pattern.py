num= int(input(">"))
n=0
for i in range(1, num+1):
    for j in range(1,(num-i)+1):
        print('-',end=' ')
        
    while n!=(2*i-1):
        print("!",end='-')
        n=n+1
    n=0
    print()

    
