'''   A A A A A
      A       A
      A       A
      A A A A A
      A       A
      A       A

'''
def A(col):
    for row in range(7):
        for j in range(col+5):
            
            if ((j==col or j==col+4) and  row!=0) or ((row==0 or row==3) and (j>=col and j<=col+4)):
                print("A",end=' ')
            
            
            else:
                print(end='  ')           
            
        print()

def B(col):
    for row in range(7):
        for j in range(col+5):
            
            if (j==col ) or (j==col+4 and (row!=0 and row!=3 and row!=6 ))or  (row==0 or row==3 or row==6) and (j>col and j<col+4)  :
                print("B",end=' ')
            else:
                print(end='  ')           
            
        print()

def C(col):
    for row in range(7):
        for j in range(col+5):
            
            if (j==col) or (row==0 or row==6) and (j>col and j<col+4):
                print("C",end=' ')
            else:
                print(end='  ')           
            
        print()


def D(col):
    for row in range(7):
        for j in range(col+5):
            
            if (j==col ) or (j==col+4 and (row!=0  and row!=6 ))or  (row==0  or row==6) and (j>col and j<col+4)  :
                print("D",end=' ')
            else:
                print(end='  ')           
            
        print()


def E(col):
    for row in range(7):
        for j in range(col+5):
            
            if (j==col ) or  (row==0 or row==3 or row==6) and (j>col and j<col+4)  :
                print("E",end=' ')
            else:
                print(end='  ')           
            
        print()


def F(col):
    for row in range(7):
        for j in range(col+5):
            
            if (j==col ) or  (row==0 or row==3 ) and (j>col and j<col+4)  :
                print("F",end=' ')
            else:
                print(end='  ')           
            
        print()
def J(col):
    #J
    for row in range(7):
        for j in range(col+5):
            if j==col+2 or (j>=col and row==0 and j!=col+2) or (row==6 and j<col+2 and j>=col):
                print("J",end=' ')
            else:
                print(end='  ')
        print()


idx=[x for x in range(100) if x%7==0 ]
print(idx)
A(0)
B(6)
C(12)
D(18)
E(24)
F(30)
J(36)
