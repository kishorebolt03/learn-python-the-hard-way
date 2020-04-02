'''
def cricket_score(balls):
    p1, p2, bench = 0, 1, 10
    scores = [0] * 11
    extras = balls.count('b') + balls.count('w')
    current_ball = 1

    for x in balls:
        swap_check = 0
        if x.isdigit():
            scores[p1] += int(x)
            swap_check = int(x) % 2
        elif x == 'O' and bench == 0:
            return scores, extras
        elif x == 'W':
            p1 = max(p1, p2) + 1
            bench -= 1
        if x != 'w':
            current_ball += 1
        if current_ball % 6 == 0 or swap_check == 1 or x == 'b':
            p1, p2 = p2, p1

    return scores, extras
'''
'''
lineScore = input("Enter score: ")
players = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,"E":0}
onBase,overCnt = [1,2],0

for c in lineScore:
    overCnt = overCnt + int(c != "w") if overCnt < 6 else 0
    if c == "W":
        onBase[0] = min(max(onBase) + 1,11)
    elif c.isdigit():
        players[onBase[0]] += int(c)
        onBase = [onBase[1],onBase[0]] if int(c) % 2 == 1 else onBase
    players["E"] += int(c == "b" or c == "w")
    if overCnt == 6 or c == "b":
        onBase.reverse()

for p in range(1,max(onBase) + 1):
    print("P" + str(p) + ":",players[p])
print("Extras:", players["E"])
'''
'''
def change(ball,run):
    if ball%6==0 or run%2!=0:
        return True
    return False
def Out(ball,p_score):


def scorer(score,p_1,p_2):
    ball=0
    exs=0
    p_curr=1
    wkt=0
    Total=0
    for i in score :
        if i=='.':
            p_1+=0
            ball+=1
        elif i=='W':
            exs+=1
            ball+=1
        elif i=='O':
            if p_curr==1:
                Out(ball,p_1)
            else:
                Out(ball,p_2)
            ball+=1
        elif i=='1' or i=='2' or i=='3' or i=='4' or  i=='6':
            if ball==0:
                p_curr=1

            if ball>0 and change(ball,int(i)):
                if p_curr==1:
                    p_curr=2
                else:
                    print("here")
                    p_curr=1

            if p_curr==1:
                p_1+=int(i)
                ball+=1
                print("P1        ",int(i),ball,p_1)
            else:
                p_2+=int(i)
                ball+=1
                print("P2        ",int(i),ball,p_2)

    print("P1  ",p_1,"P2    ",p_2)


if __name__=='__main__':

    score=list(input())
    player={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0}
    curr_S=0
    curr_NS=0
    scorer(score,0,0)
'''
'''
output for Cricket  :

input:OO15OO87OWWWWW910OOOOO23

output:

Score
P1: 0
P3: 0
P4: 1
P2: 0
P5: 0
P6: 0
P7: 1
P8: 0
P9: 0
P10: 0
P11: 0

Strike : P10
Non-Strike : P11
Total  :  7
Overs : 2.1
ex : 5
wkts : 10
Remaining wkts : 0

or

input invalid

if u consider 5 as Wide +4

Score
P1: 0
P3: 0
P4: 1
P2: 0
P5: 0
P6: 0
P7: 1
P8: 0
P9: 0
P10: 0
P11: 0

Strike : P10
Non-Strike : P11
Total  :  12
Overs : 2.1
ex : 10
wkts : 10
Remaining wkts : 0
'''

def scorer(s):
    print(s)
    d_run=['1','2','3','4','6','O','0']
    ex = [i for i in s if (i =='W')]
    wkts=10
    skip=0
    score = s.replace('W', '').replace('.', '0').replace('7','').replace('5','').replace('8','').replace('9','')
    res, pl = [], [1, 2]

    for ball, i in zip(range(1,len(score)+1),score):
        if wkts<=0:
            break

        #if i not in d_run:

            #case 1
            #print("Invalid Input",i,"in the string")
            #exit()
        if i == 'O':
            skip+=1
            print("ball========",ball,pl[0],i)
            res.append((pl[0], 0))
            pl = [max(pl) + 1, pl[1]]
            wkts-=1
            if ball % 6 == 0:
                pl = pl[::-1]
                if wkts==1:
                    pl = pl[::-1]



        elif int(i) % 2 == 0 and i in d_run:
            print("ball========",ball,pl[0],i)
            res.append((pl[0], int(i)))
            skip+=1
            if ball % 6 == 0:
                pl = pl[::-1]

        elif i in d_run:
            print("ball========",ball,pl[0],i)
            skip+=1
            res.append((pl[0], int(i)))
            pl = pl[::-1]


    d = {k:v for k, v in res}
    grouped = [(x, sum(v for k, v in res if k == x)) for x in d.keys()]
    sm=0
    print("Score")
    #print(grouped)
    for i in grouped:
        print(''.join(('P', str(i[0]), ':')), i[1])
        sm+=i[1]
    extras=0
    for i in ex:
        if i == '5' or i == '7':
            extras+=int(i)
        else:
            extras+=1
    print()
    scor_len=len(score)-skip
    if wkts>=1:
        print("Strike : P"+str(grouped[-2][0]))
    print("Non-Strike : P"+str(grouped[-1][0]))
    print('Total  : ',sm+extras)
    print('Overs :',str(skip//6)+'.'+str(skip%6))
    print('ex :', extras)
    print('wkts :',10-wkts)
    print('Remaining wkts :',wkts)

if __name__=='__main__':
    scorer("OO15OO87OWWWWW910OOOOO23")
