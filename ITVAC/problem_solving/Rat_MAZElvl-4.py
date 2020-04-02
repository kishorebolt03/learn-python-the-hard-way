import copy
maze = [
    [0,0,0,0,0],
    [0,1,0,0,0],
    [0,0,0,0,0],
    [0,1,0,1,0],
    [0,1,1,1,0]
]
N= len(maze)
solution = [[0]*N for _ in range(N)]
lis=[]
d=0
dist=[]

def solvemaze(l,r,dist):
    print("entering")
    global d
    if maze[0][0]==1 and maze[N-1][N-1]==1 and maze[0][N-1]==1 and maze[N-1][0]==1:
        print("1")
        return False
    if ((l==N-1 and r==N-1) or (l==0 and r==N-1) or(l==0 and r==0) or (l==N-1 and r==0)) and maze[l][r]!=1:
        solution[l][r]=1
        d+=1
        dist.append(d)
        lis.append(copy.deepcopy(solution))
        solution[l][r]=0
        print("inside if")
        if d not in dist:
            return True
        d-=1
        return False
    if l<N and r<N and l>=0 and r>=0 and solution[l][r]==0 and maze[l][r]==0:
        solution[l][r]=1
        d+=1
        if solvemaze(l+1,r,dist):
            return True
        if solvemaze(l,r+1,dist):
            return True
        if solvemaze(l-1,r,dist):
            return True
        if solvemaze(l,r-1,dist):
            return True

        solution[l][r]=0
        d-=1
        return False
    return 0


if solvemaze(2,0,dist)==True:
    pass
else:
    if dist!=[]:
        for i in maze:
            print(i)
        print()
        for i in lis[dist.index(min(dist))]:
            print(i)
        print()
        print("minimum distance is :",min(dist))
    else:
        print("no solution")
