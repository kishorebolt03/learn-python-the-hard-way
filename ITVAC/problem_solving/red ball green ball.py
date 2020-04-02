'''
G R G G G
R G R R G
R G G G G
G R R R G
G G R G G

GGGGR
GGGRG
GGRRG
GRGGG
RGGGG

10
RRRRRRRRRR
RRRRRRRRRG
RRRRRRRRGG
RRRRRRRGGG
RRRRRRGGGG
RRRRRGGGGG
RRRRGGGGGG
RRRGGGGGGG
RRGGGGGGGG
RGGGGGGGGG

7
GGRRRGG
RRRGGGG
RRGGRGG
GGGGGGG
RRGGGGG
GGGGGRG
RGGGGGG
'''

n=int(input())
matrix=[]
swap_cnt=0
cnt=0
for i in range(n):
    matrix.append(list(input())[:n])
for p in range(0,n):
    '''for j in range(p+1,len(matrix)):
        if matrix[p][j]=='G':
            cnt+=1
    print("---------------------------",matrix[p])
    print(cnt,matrix[p].count('G'))
    if cnt==matrix[p][p+1:].count('G'):
        continue'''

    for i in range(1,n-p):
        wt_R1=0
        wt_R2=0
        for j in range(len(matrix[i-1])):
            if matrix[i-1][j]=='R':
                wt_R1+=(j+1)*(j+1)
        for j in range(len(matrix[i])):
            if matrix[i][j]=='R':
                wt_R2+=(j+1)*(j+1)
        if wt_R1>wt_R2:
            matrix[i-1],matrix[i]=matrix[i],matrix[i-1]
            swap_cnt+=1
for i in range(len(matrix)):
    print(matrix[i])
for i in range(len(matrix)-1):
    for j in range(i+1,len(matrix)):
        if matrix[i][j]=='R':
            print("-1")
            exit()
print(swap_cnt)
