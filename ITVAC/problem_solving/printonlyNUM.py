'''
Input:
1
Hi5 welcome567 batch 2019

output:
5 567
'''


t=int(input())
for i in range(t):
    l=[]
    s=input().split()
    #print("1")
    for j in range(len(s)):
        if '9' not in s[j]:
            s1=list(s[j])
            k=0
            l1=[]
            #print("12")
            while k<len(s1):
                if s1[k].isdigit():
                    l1.append(s1[k])
                else:
                    l1.append('')
                k+=1
            l.append("".join(l1))
    print(" ".join(l))
