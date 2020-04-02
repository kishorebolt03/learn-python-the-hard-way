def sortdict(b,rev):
    a=b
    cnt=[i+1 for i in range(len(a))]
    for j in range(1,len(a)):
        if rev==True:
            if a[j-1]<a[j]:
                a[j-1],a[j]=a[j],a[j-1]
                cnt[j-1],cnt[j]=cnt[j],cnt[j-1]
        else:
            if a[j-1]>a[j]:
                a[j-1],a[j]=a[j],a[j-1]
                cnt[j-1],cnt[j]=cnt[j],cnt[j-1]

    return a

def keyfunc(tup):
    key, d = tup
    return d["eng"]


#driver
dict={'AB':{'eng':40,'sci':50},'RA':{'eng':10,'sci':40},'JE':{'eng':30,'sci':60}}
print(dict.keys())
a=[k['eng'] for k in [dict[v] for v in dict.keys()]]
'''print("average-------",sum(a)//3)


#topper
top=max(a)
for i,k in dict.items():
    for j,l in k.items():
        if j=='eng' and l==top:
            print("\n{} scored the highest\n".format(i,l))
'''
#sort
a=sortdict(a,True)
print("sorted ------ ",a)
p=0
sorted_name=[print(k) if m=='eng' and p<len(a) else '' for m,n in l.items() for k,l in dict.items()]
