from time import sleep



'''   A A A A A
      A       A
      A       A
      A A A A A
      A       A
      A       A

'''
def A(colA):
    colB=colA+7
    for row in range(7):
        for j in range(colA+7+colB):
            if ((j==colA or j==colA+4) and  row!=0) or ((row==0 or row==3) and (j>=colA and j<=colA+4)) or ((j==colB ) or (j==colB+4 and (row!=0 and row!=3 and row!=6 ))or  (row==0 or row==3 or row==6) and (j>colB and j<colB+4)):
                print("*",end=' ')
            
            else:
                print(end='  ')
        print()
'''



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

def G(col):
    for row in range(7):
        for j in range(col+5):

            if (j==col ) or  ((j==col+4) and (row!=1 and row!=2))or ((row==0 or row==6 ) and (j>col and j<col+4)) or (row==3 and (j==col+3 or j==col+5)):
                print("G",end=' ')
            else:
                print(end='  ')

        print()

def H(col):
    for row in range(7):
        for j in range(col+5):

            if ((j==col or j==col+4) and  row!=0) or ((row==3) and (j>=col and j<=col+4)):
                print("H",end=' ')
            else:
                print(end='  ')

        print()

def I(col):
    for row in range(7):
        for j in range(col+5):

            if j==col+2 or (j>=col and row==0 and j!=col+2) or (row==6 and j>=col):
                print("I",end=' ')
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

def K(col):
    l=0
    k=col+4
    for row in range(7):
        for j in range(col+5):
            if (j==col ) or (row==(j+2-col) and j>col+1)  :
                print("K",end=' ')
            elif ((row==l and j==k) and j>0):
                print("K",end=' ')
                l+=1
                k-=1
            else:
                print(end='  ')

        print()

def L(col):
    for row in range(7):
        for j in range(col+5):

            if (j==col ) or (row==6 and j>=col) :
                print("L",end=' ')
            else:
                print(end='  ')

        print()

def M(col):
    for row in range(7):
        for j in range(col+5):
            if (j==col or j==col+4) or (row<=2 and row>0 and j==col+row )or (row<3 and row>0 and  j==col+4-row) :
                print("M",end=' ')
            else:
                print(end='  ')

        print()

def N(col):
    for row in range(7):
        for j in range(col+7):

            if (j==col or j==col+6) or (row<=7 and row>0 and j==col+row ) :
                print("N",end=' ')
            else:
                print(end='  ')

        print()

def O(col):
    for row in range(7):
        for j in range(col+5):

            if (j==col and row!=0 and row!=6) or (j==col+4 and (row!=0 and row!=6 ))or  (row==0 or row==6) and (j>col and j<col+4)  :
                print("O",end=' ')
            else:
                print(end='  ')

        print()

def P(col):
    for row in range(7):
        for j in range(col+5):

            if (j==col ) or (j==col+4 and (row!=0 and row<3 ))or  (row==0 or row==3 ) and (j>col and j<col+4)  :
                print("B",end=' ')
            else:
                print(end='  ')

        print()

def Q(col):
    for row in range(8):
        for j in range(col+5):

            if (j==col and row!=0 and row<7) or (j==col+4 and (row!=0 ) and row <7)or  ((row==0 or row==6) and (j>col and j<col+4))  or (row==5 and j==col+1 ) or (row ==7 and j==col+3):
                print("O",end=' ')
            else:
                print(end='  ')

        print()

def R(col):
    for row in range(7):
        for j in range(col+5):

            if (j==col ) or (j==col+4 and (row!=0 and row!=3 ))or  (row==0 or row==3 ) and (j>col and j<col+4)  :
                print("B",end=' ')
            else:
                print(end='  ')

        print()

def S(col):
    for row in range(7):
        for j in range(col+5):

            if (j==col ) or  (row==0 or row==3 ) and (j>col and j<col+4)  :
                print("F",end=' ')
            else:
                print(end='  ')

        print()

def T(col):
    #J
    for row in range(7):
        for j in range(col+5):
            if j==col+2 or (j>=col and row==0 and j!=col+2) :
                print("T",end=' ')
            else:
                print(end='  ')
        print()

def U(col):
    for row in range(7):
        for j in range(col+5):

            if (j==col ) or  (row==0 or row==3 ) and (j>col and j<col+4)  :
                print("F",end=' ')
            else:
                print(end='  ')

        print()

def V(col):
    for row in range(7):
        for j in range(col+5):

            if (j==col ) or  (row==0 or row==3 ) and (j>col and j<col+4)  :
                print("F",end=' ')
            else:
                print(end='  ')

        print()

def W(col):
    for row in range(7):
        for j in range(col+5):

            if (j==col ) or  (row==0 or row==3 ) and (j>col and j<col+4)  :
                print("F",end=' ')
            else:
                print(end='  ')

        print()

def X(col):
    for row in range(7):
        for j in range(col+5):

            if (j==col ) or  (row==0 or row==3 ) and (j>col and j<col+4)  :
                print("F",end=' ')
            else:
                print(end='  ')

        print()

def Y(col):
    for row in range(7):
        for j in range(col+5):

            if (j==col ) or  (row==0 or row==3 ) and (j>col and j<col+4)  :
                print("F",end=' ')
            else:
                print(end='  ')

        print()

def Z(col):
    for row in range(7):
        for j in range(col+5):

            if (j==col ) or  (row==0 or row==3 ) and (j>col and j<col+4)  :
                print("F",end=' ')
            else:
                print(end='  ')

        print()



'''

idx=[x for x in range(100) if x%7==0 ]
A(0)
sleep(0.5)
B(6)
sleep(0.5)
C(12)
sleep(0.5)
D(18)
sleep(0.5)
E(24)
sleep(0.5)
F(30)
sleep(0.5)
G(35)
sleep(0.5)
H(40)
sleep(0.5)
I(46)
sleep(0.5)
J(52)
sleep(0.5)
K(58)
sleep(0.5)
L(64)
sleep(0.5)
M(70)
sleep(0.5)
N(76)
sleep(0.5)
O(70)
sleep(0.5)
P(64)
sleep(0.5)
Q(58)
sleep(0.5)
sleep(0.5)
sleep(0.5)
sleep(0.5)
sleep(0.5)
sleep(0.5)
sleep(0.5)
sleep(0.5)
sleep(0.5)
sleep(0.5)
