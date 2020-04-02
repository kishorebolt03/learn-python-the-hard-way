'''
3
4
C1 100 300
C2 100 300
C3 100 200
C4 100 400
4
F_C1
F_C2
C2_C3
C3_C4
'''



total = 0
days=int(input())
C_def=[input() for i in range(int(input()))]
L_def=[input() for i in range(int(input()))]
d={}
for i in C_def:
    i=i.split(' ',2)
    d[i[0]]=[list(map(int,i[1:])),[int(i[-1])]]
    total+=int(i[-1])

links=[]
for i in L_def:
    if i.startswith('F'):
        links.append([i.split('_')[1]])
    else:
        s=i.split('_')
        for l in links:
            if i.split('_')[0] in l:
                l.append(i.split('_')[1])

#print(links)
#print(d)
drained = []
while days-1:
    for k,v in d.items():
        #print("test---------",v[1],v[0])
        v[1]=[v[1][0]-v[0][0]]
        #print(v[1])
        #print(d)
    for k,v in d.items():
        #print("test1---------",v[1],v[0])
        if v[1][0]<v[0][0]:
            drained.append(k)
    for i in links:
        for j in drained:
            if i.__contains__(j):
                ind=i.index(j)
                for k in range(ind+1):
                    d[i[k]][1]=[d[i[k]][0][1]]
                    total+=d[i[k]][0][1]
    #print(drained)
    days-=1
print(total)
