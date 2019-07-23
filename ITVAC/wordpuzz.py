

M=4
N=3
k=0
visited=[[0,0,0,0],[0,0,0,0],[0,0,0,0]]

def search(mat,i,j,visited,ch):

    if i>=0 and j>=0 and i<M and j<N and visited[i][j]==0:
        if ch[k]==mat[i][j]:
            j+=1
            k+=1
            visited[i][j]==1
            return search(mat,i,j,visited,ch)
        else:




def display():



n=input().upper()
mat=[  ['A','B','C','I'],
        ['S','I','C','S'],
        ['E','D','E','E']
        ]
ch=list(n)
search(n,mat)
#print mat
