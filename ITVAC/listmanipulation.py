def qsort(inlist):
    if inlist == []:
        return []
    else:
        pivot = inlist[0]
        lesser = qsort([x for x in inlist[1:] if x < pivot])
        greater = qsort([x for x in inlist[1:] if x >= pivot])
        return greater + [pivot] + lesser

n= int(input())

lst=[]

for i in range(n):
    b=int(input())
    lst.append(b)

pvt=int(input())
lst1=[]
lst2=[]
lst3=[]
print(lst1)
print(lst2)
print(lst3)
for i in lst:
    if i>pvt:
        lst1.append(i)
        print("1")
    elif i<pvt:
        lst2.append(i)
        print("2")
    else:
        lst3.append(i)
        print("3")
newlst=qsort(lst2)+lst3+qsort(lst1)
print(newlst)
