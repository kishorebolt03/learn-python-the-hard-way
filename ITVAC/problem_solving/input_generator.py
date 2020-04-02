import random
from itertools  import combinations_with_replacement as C



st='''
Lorem ipsum dolor sit'''
st=st.split()
s=C(st,37)
cnt=0
with open("testcase.txt",'w') as File:
    for i in list(s):
        File.write(" ".join(i))
        cnt+=1
    File.write("\n")
print(cnt)
