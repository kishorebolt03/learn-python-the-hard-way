string='''00:05:17,959-720-018
00:21:38,750-222-197
00:13:21,959-720-018
00:17:01,892-545-277'''

log=string.split("\n")
dic={}
numbers=[]
for i in log:
    s=i.split(',')
    time=s[0].split(":")
    time=[int(x) for x in time]
    t=time[0]*3600 + time[1]*60+time[2]
    numbers.append(s[1])
    if s[1] in dic.keys():
        t=dic[s[1]]+t

    dic.update({s[1]:t})
call=[]
new_dic={}
for i,j in [[x[0],x[1]] for x in sorted(dic.items(),key=lambda kv: kv[1],reverse=True)]:
    new_dic[i]=j
for k,v in dic.items():
    mi=0
    if dic[k]<300:
        call.append([k,dic[k]*3])
        dic[k]=dic[k]
    else:
        if dic[k]%60==0:
            mi=dic[k]//60
        else:
            mi=dic[k]//60+ numbers.count(k)
            #print("k+++++++++++++++",numbers.count(k))
            #print("mi",mi,dic[k])
        call.append([k,mi*150])
        dic[k]=mi

M=list(new_dic.values()).count(max((new_dic.values())))
sm=0
if M==1:
    k=[sorted(new_dic.items(),key=lambda kv: kv[1],reverse=True)][0][0][0]
    #print('k===',k)
    for i in range(len(call)):
        if call[i][0]==k:
            call[i][1]=0
    for i in range(len(call)):
        sm+=call[i][1]
    #print(new_dic)
    #print(call)
    print(sm)


else:
    mx=[sorted(new_dic.items(),key=lambda kv: kv[1],reverse=True)][0][0][1]
    #print('max',mx)
    arr=[]
    #print(new_dic)
    for i,j in sorted(new_dic.items(),key=lambda kv: kv[1],reverse=True):
        if j==mx:
            arr.append(i)
    arr.sort()
    for i in call:
            if i[0]==arr[0]:
                i[1]=0
    for i in call:
        sm+=i[1]
    #print(call)
    print(sm)
