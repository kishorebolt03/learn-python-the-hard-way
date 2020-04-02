# inputv='''
# 3
# .X.
# 4
# X.X.
# 4
# .XX.
# '''.splitlines()
# inputc=0
# def input(a=None):
#  global inputc
#  if a:print(a,end='')
#  inputc+=1
#  return inputv[inputc]

def wheel():
 n=int(input())
 w=list(input())
 s=0
 v=[]
 for z in range(n-w.count('X')):
  for k,i in enumerate(w):
   w3=w[k:]+w[:k]
   for k2,j in enumerate(w3):
    if j.startswith('.'):
     v.append(n-k2);
     w2=list(w);
     w2[(k+k2)%n]='X';
     break
  else:
   w[w.index('.')]='X'

 print(f'{sum(v)/n:.5f}')

for i in range(1):wheel()
