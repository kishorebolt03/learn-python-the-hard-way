def convert(list):
    s = [str(i) for i in list]
    res = " ".join(s)
    return(res)


n = input().split()
k=list(n)

print(convert(k[::-1]))
