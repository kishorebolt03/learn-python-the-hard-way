from time import sleep
from threading import Thread as T
from multiprocessing import Process
import sys

result=''

def Letter(col,l):
    global result
    for row in range(7):
        for j in range(col+20):
            a=(((j==colA or j==colA+4) and  row!=0) or ((row==0 or row==3) and (j>=colA and j<=colA+4)))
            b=((j==colB ) or (j==colB+4 and (row!=0 and row!=3 and row!=6 ))or  (row==0 or row==3 or row==6) and (j>colB and j<colB+4))
            c=((j==colC) or (row==0 or row==6) and (j>colC and j<colC+4))
            d=((j==colD ) or (j==colD+4 and (row!=0  and row!=6 ))or  (row==0  or row==6) and (j>colD and j<colD+4))
            e=((j==colE ) or  (row==0 or row==3 or row==6) and (j>colE and j<colE+4))
            f=((j==colF ) or  (row==0 or row==3 ) and (j>colF and j<colF+4))
            g=((j==colG ) or  ((j==colG+4) and (row!=1 and row!=2))or ((row==0 or row==6 ) and (j>colG and j<colG+4)) or (row==3 and (j==colG+3 or j==colG+5)))
            h=(((j==colH or j==colH+4) and  row!=0) or ((row==3) and (j>=colH and j<=colH+4)))
            i=(j==colI+2 or (j>=colI and row==0 and j!=colI+2) or (row==6 and j>=colI))
            j=(j==colJ+2 or (j>=colJ and row==0 and j!=colJ+2) or (row==6 and j<colJ+2 and j>=colJ))
            k=(" ")
            l=((j==colL ) or (row==6 and j>=col))
            m=((j==colM or j==col+4) or (row<=2 and row>0 and j==col+row )or (row<3 and row>0 and  j==col+4-row))
            n=((j==colN or j==col+6) or (row<=7 and row>0 and j==col+row ))
            o=((j==colO and row!=0 and row!=6) or (j==col+4 and (row!=0 and row!=6 ))or  (row==0 or row==6) and (j>col and j<col+4))
            p=((j==colP ) or (j==col+4 and (row!=0 and row<3 ))or  (row==0 or row==3 ) and (j>col and j<col+4))
            q=((j==colQ and row!=0 and row<7) or (j==col+4 and (row!=0 ) and row <7)or  ((row==0 or row==6) and (j>col and j<col+4))  or (row==5 and j==col+1 ) or (row ==7 and j==col+3))
            r=((j==colR ) or (j==col+4 and (row!=0 and row!=3 ))or  (row==0 or row==3 ) and (j>col and j<col+4))


            if a and l=='A':
                result=result+"A "
            if b and l=='B':
                result+="B "
            if a!=True and b!=True:
                result+="  "
        result+="\n"


if __name__=='__main__':
    col=0
    r=input().split()
    with open("new.txt", "w") as textfile:
        Letter(0,r[0])
        print(result)
        textfile.write(result)
        result=''
        textfile.seek(0,0)
        '''Letter(7,r[1])
        print(result)
        textfile.write(result)'''
        print("file updated")
    textfile.close()
