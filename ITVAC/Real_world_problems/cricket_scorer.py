'''
3.Cricket Score
Design a cricket dashboard using the input string as the runs.
W - Wide
O - Out
. – Dot
1,2,3,4,6(runs)
P1…..P11=Player 1 to Player 11
Example:1
Input: …222431666
Output:
P1 – 7(runs)
P2 – 25(runs)
Strike – P1
Non-Strike-P2
Total-32
Overs-2
Extra-0
Wicket(s)-0
Remaining Wickets(s)-10
Example:2
Input: WWW…23O11..46

Output:
P1 – 16(runs)
P2 – 0(runs)
P3 – 1(runs)
Strike – P3
Non-Strike-P1
Total-20
Overs-2
Extra-3
Wicket(s)-1
Remaining Wickets(s)-9
Note:Consider player change the strike for every Over (6 balls).Add one run and one ball
to wide. Wide run will not consider under the individual player score.Wide runs consider
only as Extra. Total score includes all player individual runs and Extra runs.
Test case 1:
Input :
...222431666

Output :
P1-7(runs)
P2-25(runs)
Strike-P1
Non-Strike-P2
Total-32
Overs-2.0
Extra-0
Wicket(s)-0
Remaining Wicket(s)-10
Test case 2:
Input :
46112W1
O166O.
21143O

Output :

P1-14(runs)
P2-13(runs)
P3-11(runs)
P4-1(runs)
P5-0(runs)
Strike-P3
Non-Strike-P5
Total-40
Overs-3.0
Extra-1
Wicket(s)-3
Remaining Wicket(s)-7
Test case 3:
Input :
WWW...23O11..46

Output :
P1-16(runs)
P2-0(runs)
P3-1(runs)
Strike-P3
Non-Strike-P1
Total-20
Overs-2.0
Extra-3
Wicket(s)-1
Remaining Wicket(s)-9
'''

def scorer(s):
    ex = [i for i in s if i =='W']
    wkts=10
    score = s.replace('W', '').replace('.', '0')
    res, pl = [], [1, 2]

    for ball, i in zip(range(1,len(score)+1),score):
        if i == 'O':
            res.append((pl[0], 0))
            pl = [max(pl) + 1, pl[1]]
            wkts-=1
        elif int(i) % 2 == 0:
            res.append((pl[0], int(i)))
            if ball % 6 == 0:
                pl = pl[::-1]
        else:
            res.append((pl[0], int(i)))
            pl = pl[::-1]

    d = {k:v for k, v in res}
    grouped = [(x, sum(v for k, v in res if k == x)) for x in d.keys()]
    sm=0
    print("Score")
    print(grouped)
    for i in grouped:
        print(''.join(('P', str(i[0]), ':')), i[1])
        sm+=i[1]
    print()
    print("Strike : P"+str(grouped[-2][0]))
    print("Non-Strike : P"+str(grouped[-1][0]))
    print('Total  : ',sm+len(ex))
    print('Overs :',str(len(score)//6)+"."+str(len(score)%6))
    print('ex :', len(ex))
    print('wkts :',10-wkts)
    print('Remaining wkts :',wkts)

if __name__=='__main__':
    scorer("OO1OO")
