#include<stdio.h>
#define N 55
#define true 1
#define false 0

int m,n;

void movemonsters(char a[N][N])
{
    int i,j;
    for(i=1;i<=m;++i)
    {
        if(i%2 == 0) //move right
        {
         char temp = a[i][n-1];
         for(j = n-1;j>=0;j--)
            a[i][j] = a[i][j-1];
         a[i][0] = temp;
        }
        else //move left
        {
            char temp = a[i][0];
            for(j = 0;j<n-1;j++)
                a[i][j] = a[i][j+1];
            a[i][n-1] = temp;
        }
    }
}

int solveMazeUtil(char maze[N][N], int x, int y, char sol[N][N],int count);

/* A utility function to print solution matrix sol[N][N] */
void printSolution(char sol[N][N])
{
    for (int i = 0; i < m+1; i++) {
        for (int j = 0; j < n; j++)
            printf(" %d ", sol[i][j]);
        printf("\n");
    }
}

/* A utility function to check if x, y is valid index for N*N maze */
int isSafe(char maze[N][N], int x, int y)
{
    // if (x, y outside maze) return false
    if (x >= 0 && x <= m+1 && y >= 0 && y < n && /* maze[x][y] != 1 && */maze[x][y] != 'X')
        return true;

    return false;
}

/* This function solves the Maze problem using Backtracking.  It mainly
   uses solveMazeUtil() to solve the problem. It returns false if no
   path is possible, otherwise return true and prints the path in the
   form of 1s. Please note that there may be more than one solutions,
   this function prints one of the feasible solutions.*/
int solveMaze(char maze[N][N])
{
    char sol[N][N] = { { 0, 0, 0, 0 },
                      { 0, 0, 0, 0 },
                      { 0, 0, 0, 0 },
                      { 0, 0, 0, 0 } };

   /* 0,0 is the initial position of the prince */
    if (solveMazeUtil(maze, 0, 0, sol,0) == false) {
        printf("Impossible");
        return false;
    }

    //printSolution(sol);
    return true;
}



/* A recursive utility function to solve Maze problem */
int solveMazeUtil(char maze[N][N], int x, int y, char sol[N][N],int count)
{
    static int prevx, prevy;
    static int cnt = 0;
    static int waitcount = 0;

    // if (x, y is goal) return true
    if (x == m+1 && y == n-1) {
        sol[x][y] = 1;
        printf("%d\n",count);
        return true;
    }

    if(prevx == x && prevy == y)
        cnt++;
    else
    {
        prevx = x;
        prevy = y;
        cnt = 0;
    }


    // Check if maze[x][y] is valid
    if (isSafe(maze, x, y) == true) {
        // mark x, y as part of solution path

        sol[x][y] = 1;

        movemonsters(maze);

        /* Move forward in x direction */
        if (solveMazeUtil(maze, x + 1, y, sol,count+1) == true)
            return true;

        /* If moving in x direction doesn't give solution then
           Move down in y direction  */
        if (solveMazeUtil(maze, x, y + 1, sol,count+1) == true)
            return true;


        /* Stay at same position */
        if (count < n && solveMazeUtil(maze, x, y, sol,count+1) == true)
            return true;


        /*if (solveMazeUtil(maze, x, y - 1, sol,count+1) == true)
            return true;

        if (solveMazeUtil(maze, x-1, y, sol,count+1) == true)
            return true; */

        /* If none of the above movements work then BACKTRACK:
            unmark x, y as part of solution path */

        sol[x][y] = 0;
        return false;
    }

    return false;
}

void main()
{
    int i;
    char a[N][N];
    char soln[N][N];

    scanf("%d %d\n",&m,&n);
    //printf("%d %d\n",m,n);

    for(i=0;i<=m+1;++i)
        gets(a[i]);

    //printarray(a);
    solveMaze(a);

}
