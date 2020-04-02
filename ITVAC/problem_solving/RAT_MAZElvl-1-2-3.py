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
