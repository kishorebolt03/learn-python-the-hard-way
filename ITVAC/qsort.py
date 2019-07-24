def qsort(inlist):
    if inlist == []:
        return []
    else:
        pivot = inlist[0]
        lesser = qsort([x for x in inlist[1:] if x < pivot])
        greater = qsort([x for x in inlist[1:] if x >= pivot])
        return greater + [pivot] + lesser




n=[1,2,4,5,6,8,3,5,10,8,9,0]
print(qsort(n))
