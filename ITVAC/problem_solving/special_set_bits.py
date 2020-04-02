

def solve (R, L):
    # Write your code here
    global primes
    cnt=0
    for i in range(L,R+1):
        if i==1 or i==0:
            continue
        a=bin(i).replace('0b','')[::-1]
        #print(a)
        fl=0
        #print(list(filter(lambda x: x<=len(a),primes)))
        for j in list(filter(lambda x: x<=len(a),primes)):
            if a[j-1]=='1':
                cnt+=1
    return cnt


T = int(input())
primes = [2,3,5,7,11,13,17]
r=0
for _ in range(T):
    L ,R = map(int,input().split())
    out_ = solve(R, L)
    print (out_)
