


def freq(n):
    cnt=[]
    w=set(n)
    o=list(w)
    for i in range(len(o)):
        cnt.append(0)
    #print(o)
    if len(n)>0 and len(n)<100:
        k=list(n)
        q=0
        for i in range(len(o)):
            for j in range(len(n)):
                if o[i]==k[j]:
                    cnt[i]+=1
    else:
        print(o[1],":",cnt[1])
        print("empty string")
        return 0
    for c in range(1,len(cnt)):
        for t in range(len(cnt)-1):
            if cnt[t]>cnt[c]:
                cnt[c],cnt[t]=cnt[t],cnt[c]
                o[c],o[t]=o[t],o[c]
    print(o)
    print(cnt)
    g=len(cnt)
    flag=0
    if len(cnt)>2 :
        v=0
        while cnt[v]<cnt[g-1]:
            v+=1

        if cnt[v-1]==cnt[v-2]:
            print("no 2nd most in string")

        else:
            print(o[v-1],":",cnt[v-1])
        return 0
    else:
        print(o[v-1],":",cnt[v-1])




#driver

n=input()
freq(n)
