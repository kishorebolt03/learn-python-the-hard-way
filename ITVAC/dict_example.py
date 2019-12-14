import functools

#driver
dict={'AB':{'eng':40,'sci':50},'RA':{'eng':10,'sci':40},'JE':{'eng':30,'sci':60}}
print("average ------",sum([k['eng'] for k in [dict[v] for v in dict.keys()]])//len(dict))


print((functools.reduce(lambda a,b:a+b,[y['eng'] for x,y in dict.items()]))//len(dict),"average")


#topper
print("highest is ",[ sorted(dict.items(), key=lambda kv: kv[1]['eng']
                             ,reverse=True)][0] )

#sort

print([[x[0],x[1]['eng']] for x in sorted(dict.items(),
                                          key=lambda kv: kv[1]['eng'] ,reverse=True)])

#passed
print("passed in eng \n")
print(list(filter(lambda x:x[1]>50,[list(x) for x in sorted(dict.items(), key=lambda kv: kv[1]['eng'] ,reverse=True)])))


