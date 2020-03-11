# Smallest substring
#input : only one line of string with lower case English alphabets
# constrains : 1<= len(s) <=10^5


from itertools import groupby
l=set()
def find(s):
    global l
    return len(max((list(j) for i,j in groupby(s,key=find1)),key=len))
def find1(x):
    if x in l:
        l.clear()
        return False9
        
    l.add(x)
    return True
if __name__=='__main__':
    print(find(input()))
