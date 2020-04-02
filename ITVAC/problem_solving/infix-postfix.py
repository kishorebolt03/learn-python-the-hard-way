S=input()
pres={'+':0,'-':0,'/':1,'*':1,'^':2}
stk = []
res=[]


def prec(top,curr):
    if pres[top]<pres[curr]:
        return False
    return True
for i in S:
    if i == ' ':
        continue
    if i.isalpha():
        res.append(i)
    elif i in pres.keys():
        while stk and stk[-1]!='(' and prec(stk[-1],i):
            res.append(stk.pop())
        stk.append(i)
    elif i == '(':
        stk.append(i)
    elif i==')' :
        while stk and stk[-1]!='(':
            res.append(stk.pop())
        stk.pop()
while stk:
    res.append(stk.pop())
print(res)
while 
