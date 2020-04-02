#sorting (NESTED DICTionary)

dict=
{
	'AB':{'eng':40,'sci':50},
	'RA':{'eng':10,'sci':40},
	'JE':{'eng':30,'sci':60}
}
#using predefined func
l=[]
for k ,v in dict.items():
    l.append(v['eng'],k)
    print(sorted(l))


#using userdefined func
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

#using lambda func
print([[x[0],x[1]['eng']] for x in sorted(dict.items(),key=lambda kv: kv[1] ,reverse=True)])


#HIGHEST of values in a class
def highest():
'''
    l=[]
    for k,v in d.items():
        l.append([v['Eng'],k])
    print(max(l))

'''
#using lambda func

sub=input("Enter subject to get highest scored student based on it\n")
print(sorted(d.items(), key=lambda x:x[1][sub],reverse=True)[0][0])


#AVERAGE of values of specific subjects in a class
def average():
    avg=0
    for i in d.values():
        avg+=i['Eng']
    print(avg//len(d))

#using lambda func
print((functools.reduce(lambda a,b:a+b,[y['eng'] for x,y in dict.items()]))//len(dict),"average")



#using sum func
print("average ------",
sum([k['eng'] for k in [d[v] for v in d.keys()]])//len(d))
