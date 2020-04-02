s=input()
bol=[]
for i in range(len(s)):
    if s[i].isdigit():
        for j in range(i+1,len(s)):
            if s[j].isdigit():
                if int(s[i])+int(s[j])==10:
                    if s[i:j].count('?')==3:
                        bol.append("true")
                    else:
                        bol.append('false')

if 'false' in bol:
    print(False)
else:
    print(True)
