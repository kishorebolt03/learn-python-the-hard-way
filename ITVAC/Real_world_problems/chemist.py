'''
CHEMIST QUESTION

You have been hired as a software consultant at a chemist. The chemist shop sells various types of
compounds and mixture to their customers. They have a research team that put together various formulas
for the chemist of sell. The owner of the shop is a bit of stickler for cleanliness and is also afraid of
unforeseen reactions when creating the compounds. So,she has created a rule where a new mixing can is to
used for creating a new compound (whether the compound is made of the base elements or from another
set of pre-made compounds). Your job as a consultant is to determine the minimal number of bowls that
are required to make them. Any compound/element that is part of a definition, without its own definition
can be assumed to be a base element. base elements don’t need any preparation.

Multiline input. Where first line N specifies the number of compound definitions followed by N definitions.
Followed. Followed by integer M specifies the number of compounds to prepare and M compounds
to prepare.

Calculate the minimum number of bowls required to prepared the given compounds.

Test case 1

Input
2
H2O = H + O
NaCL= Na + CL
1
NaCL
Output
1

Test case 2

Input 
2
H2O = H + O
NaCL= Na + CL
2
NaCL
NaCL
Output

1
Test case 3
Input 
4
H2O = H + O
NaCL = Na + CL
H2SO4 = H2O + S03
S03 = S + O
1
H2SO4

Output
3

'''
d={}
cnt=0
ct=0
def solve(st2):
    global cnt,d
    if st2 not in d.keys():
        #print(cnt)
        return True
    if st2 in d.keys():
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
H2SO4 = H2O + S03
S03 = S + O'''

st2='''H2SO4'''
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
    cnt=0
    solve(i)
    ct+=cnt
print(ct)
