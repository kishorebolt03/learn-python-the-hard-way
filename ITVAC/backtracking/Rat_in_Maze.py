#LEVEL-1,2,3:
import copy

maze = [
    [0,0,0,0,0],
    [0,1,0,1,0],
    [0,1,1,0,0],
    [0,0,0,0,1],
    [1,1,0,0,0]
]
SIZE= len(maze)
d=0
mindis=[]
solution = [[0]*SIZE for _ in range(SIZE)]
lis=[]
dummy=[]

def solvemaze(l,r,solution):
    global d
    if l==SIZE-1 and r==SIZE-1:
        d+=1
        solution[l][r]=1
        mindis.append(d)
        dis=0
        lis.append(copy.deepcopy(solution))
        for i in solution:
            print(i)
        print()
        if(d not in mindis):
            return True
        d-=1
        return False

    if l<SIZE and r<SIZE and l>=0 and r>=0 and solution[l][r]==0 and maze[l][r]==0:
        solution[l][r]=1
        d+=1
        if solvemaze(l+1,r,solution):
            return True
        if solvemaze(l,r+1,solution):
            return True
        if solvemaze(l-1,r,solution):
            return True
        if solvemaze(l,r-1,solution):
            return True
        solution[l][r]=0
        d-=1
        return False
    return 0

if solvemaze(0,0,solution)==True:
    pass
else:
    if(mindis==[]):
        print("no solution")
    else:
        print("lis")
        for i in lis[mindis.index(min(mindis))]:
            print(i)

        print("length is ",min(mindis))

    
    
#LEVEL-4
maze = [
    [0,0,1,0,0],
    [0,1,0,0,0],
    [0,0,0,0,0],
    [0,1,0,1,0],
    [0,1,1,1,0]
]
N= len(maze)
dist=[0]
solution = [[0]*N for _ in range(N)]

def solvemaze(l,r,dist):
    if maze[0][0]==1 and maze[N-1][N-1]==1 and maze[0][N-1]==1 and maze[N-1][0]==1:
        return False
    if ((l==N-1 and r==N-1) or (l==0 and r==N-1) or(l==0 and r==0) or (l==N-1 and r==0)) and maze[l][r]!=1:
        solution[l][r]=1
        dist[0]+=1
        return True
    if l<N-1 and r<N-1 and l>=0 and r>=0 and solution[l][r]==0 and maze[l][r]==0:
        solution[l][r]=1
        dist[0]+=1
        if solvemaze(l-1,r,dist):
            return True
        if solvemaze(l,r-1,dist):
            return True
        if solvemaze(l+1,r,dist):
            return True
        if solvemaze(l,r+1,dist):
            return True
        
        solution[l][r]=0
        dist[0]-=1
        return False
    return 0


if solvemaze(2,3,dist):
    for i in maze:
        print(i)
    print()
    for i in solution:
        print(i)
    print()
    print("minimum distance is :",dist[0])
else:
    print("no solution")
