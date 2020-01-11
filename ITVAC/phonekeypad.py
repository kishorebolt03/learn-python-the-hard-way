def combine(inp,n,d):
    l=[]
    q=['']

    while q!=[]:
        s=q.pop()
        if len(s)==n:
            l.append(s)
        else:
            for i in d[inp[len(s)]]:
                q.append(s+i)
    return l


#driver
if __name__=='__main__':
    inp=list(input())
    inp=[int(x) for x in inp]
    n=len(inp)
    d=['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
    l=combine(inp,n,d)
    print(" ".join(l))
    
    
