from collections import OrderedDict as O


#INPUT
total = 0
days = int(input())
C_def=[input() for i in range(int(input()))]
L_def = [input() for i in range(int(input()))]
d=O()
#Storing
for i in C_def:
    i=i.split(' ',2)
    d[i[0]]=[list(map(int,i[1:])),[int(i[-1])]]
    total+=int(i[-1])
#Linking
links=[]
for i in L_def:
    if i.startswith('F'):
        links.append([i.split('_')[1]])
    else:
        s=i.split('_')
        for l in links:
            if i.split('_')[0] in l:
                l.append(i.split('_')[1])
#Draining
while days-1:
    drained =[0 for i in range(len(links))]
    for k,v in d.items():
        v[1] = [v[1][0] - v[0][0]]
    for k,v in d.items():
        #print(v[1][0])
        if v[1][0]<v[0][0]:
            for p,i in enumerate(links):
                if k in i:
                    drained[p]=k
    #print(drained)
    for j in drained:
        for i in links:
            if j and j in i:
                ind=i.index(j)
                for k in range(ind+1):
                    #print("refill ===== ",d[i[k]][0][1],k,j)
                    d[i[k]][1] = [d[i[k]]][0][1]
                    total+=d[i[k]][0][1]
    #print(drained)
    days-=1
print(total) 
