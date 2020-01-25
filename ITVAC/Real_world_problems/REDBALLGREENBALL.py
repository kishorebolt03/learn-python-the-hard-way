'''
Problem 1: Red Green ball:
Red and Green Balls You have a square grid (NxN). Each cell of the grid has either a red ball or
a green ball. Your job is to arrange the balls in such a way that all the red balls are either on or
below the main diagonal. The main diagonal starts from cell 1x1 and ends at cell NxN. You have
only one move which is to swap adjacent rows. You need to achieve the final arrangement in
minimal number of moves. If it is not possible to come to a resolution by swapping then print -1
Input:
First line of input is the number of rows in grid. Rest are the lines in the grid
Output:
Minimum number of moves
Sample I/O:
Input 1:
2
RG
RR
Output:
0
Input 2:
GR
RG
Output:
1

I/P
5

GRRRR
GRRRG
GRGRR
GRRGG
GGGGG

O/P
-1
I/P
5
GRGGG
RGRRG
RGGGG
GRRRG
GGRGG
O/P
4

I/P
2
RG
RR

O/P
0

I/P
2
GR
RG

O/P
1

I/P
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
GGGGGGGGGR
O/P
-1

 

 

I/P

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

O/P

45

 

 

I/P

7

GGRRRGG

RRRGGGG

RRGGRGG

GGGGGGG

RRGGGGG

GGGGGRG

RGGGGGG

O/P

10


'''

n=int(input())
matrix=[]

swap_cnt=0
for i in range(n):
    matrix.append(list(input())[:n])
for p in range(0,n):
    for i in range(1,n-p):
        wt_R1=0
        wt_R2=0
        for j in range(len(matrix[i-1])):
            #print("in for 1",j)
            #print("in matrix1",matrix[i][j])
            if matrix[i-1][j]=='R':
                #print("in-if 1")
                #print(matrix[i-1])
                wt_R1+=(j+1)*(j+1)
                #print("wt=========",wt_R1)
        for j in range(len(matrix[i])):
            #print("in for 2")
            #print("in matrix",j)
            if matrix[i][j]=='R':
                #print("in-if 2")
                #print(matrix[i])
                wt_R2+=(j+1)*(j+1)
                #print("wt2========",wt_R2)
        #print(wt_R1,wt_R2)
        #print("-------------------------------------",)
        if wt_R1>wt_R2:
            #print("swap")
            matrix[i-1],matrix[i]=matrix[i],matrix[i-1]
            swap_cnt+=1
for i in range(len(matrix)):
    print(matrix[i])

for i in range(len(matrix)-1):
    for j in range(i+1,len(matrix)):
        #print(matrix[i][j])
        if matrix[i][j]=='R':
            print("-1")
            exit()
print(swap_cnt)
