'''
Ashish and Jeel are playing a game. They are given a multiset of arrays (initially only one array is present).

A player has to make the following move in their turn:

Select one of the arrays of size greater than 1
Divide the array into two non-empty parts such that every element of the left array is smaller than every element of the right array.
Formally, if we split an array A of size into arrays L and R, then the following conditions must hold:

L must be a non-empty prefix and R must be the remaining non-empty suffix of the array A respectively.
For every element Pi of L and every element Qj of R, the inequality Pi<Qj must hold.


A player loses if he cannot make a move. Both the players play the game optimally. If Jeel plays first, then determine who wins the game.

Input format

First line: An integer T denoting the number of test cases
Each test case:
First line: An integer N denoting the size of the array
Second line: N space separated integers, the ith integer being Ai
Output format

For each test case, print the winner of the game "Jeel" or "Ashish" (without quotes).

Answer for each test case should come in a new line.

Input Constraints

1≤T≤10

1≤N≤105

1≤Ai≤109

Time complexity question

Explanation for sample input:

In the first testcase, no matter what move Jeel makes first, Ashish can always make the second move, and Jeel will be left with 3 arrays of size 1. Hence Ashish wins.

In the second testcase, Jeel cannot make any move in the first turn itself, and hence he loses.

In the third testcase, there is only one possible move, and after Jeel cut the array into [1, 1] and [3], Ashish cannot make any move, and he loses.

'''
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
