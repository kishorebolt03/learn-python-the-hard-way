#()()()(()())
#(a(s'('ab)) === (a(sab))
st=input()
n=len(st)
tempst=st
while tempst!='':
    start=st.find('(')
    end = st.find(')')
    cnt=tempst.count('(')
    cnt1=tempst[ebd+1:].count(')')
    if cnt==cnt1:
        tempst=tempst[end+1:]
        
