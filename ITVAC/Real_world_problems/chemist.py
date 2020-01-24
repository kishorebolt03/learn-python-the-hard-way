'''
5
H2O = H + O
NaCL = Na + CL
H2SO4NaCL = H2OSO4 + NaCL
H2SO4 = H2O + SO3
H2Na = H2 + Na
2
H2SO4NaCL
H2Na
'''
d={}
cnt=0
ct=0
lis=[]
def solve(st2):
    global cnt,d
    if st2 not in d.keys() :
        #print(cnt)
        return True
    if st2 in d.keys():
        if st2 not in lis:
            lis.append(st2)
            cnt+=1
        #print("inside else")
        l=d[st2]
        #print(l)
        if solve(l[0]) or solve(l[1]):
            #print("if")
            return False
    return False


t1=3
st='''H2O = H + O
NaCL = Na + CL
H2SO4 = H2O + SO3
H2Na = H2 + Na
SO3 = S + O'''

st2='''H2SO4
NaCL'''
st=st.split('\n')
st2=st2.split("\n")
st2=list(set(st2))
for i in st:
    try:
        i=i.split(" = ")
        d[i[0]]=i[1].split(" + ")
    except:
        pass
print(d)
for i in st2:
    solve(i)
print(cnt)
