'''
1.Dictionary of Words

Given a string s and a dictionary of words dict, add spaces in s to construct a sentence
where each word is a valid dictionary word.
Return all such possible sentences.
For example, given
s = &quot;snakesandladder&quot;,
dict = [&quot;snake&quot;, &quot;snakes&quot;, &quot;and&quot;, &quot;sand&quot;, &quot;ladder&quot;].
A solution is [&quot;snakes and ladder&quot;, &quot;snake sand ladder&quot;].
Input:
The first line contains an integer T, denoting the number of test cases.
Every test case has 3 lines.
The first line contains an integer N, number of words in the dictionary.
The second line contains N strings denoting the words of the dictionary.
The third line contains a string s.
Output:
For each test case, print all possible strings.
Testcase1:
Input:
1
5
snake snakes and sand ladder
snakesandladder
Output:
snake sand ladder
snakes and ladder
Testcase2:
Input :
1
5
lr m lrm hcdar wk
hcdarlrm

Output :

hcdar lr m
hcdar lrm
Testcase 3:
Input :
1
6
hi how are you ho ware
hihowareyou
Output :
hi ho ware you
hi how are you
Testcase 4:
Input :
1
7
money best is mon ey i sbest
moneyisbest

Output :
mon ey i sbest
mon ey is best
money i sbest
money is best

not in new_dic and tmp
'''
import copy
old_dic=[]
def check(string,dic):
    all_dic=[]
    new_dic=[]
    while dic not in old_dic:
        temp=string
        new_dic=[]
        tmp=''
        i=0
        while temp!='' and i<len(string):
            tmp+=string[i]
            if tmp in dic and tmp not in all_dic:
                new_dic.append(tmp)
                temp.replace(tmp,'')
                tmp=''
            i+=1
        if new_dic==[]:
            break
        print()
        print(" ".join(new_dic))
        old_dic.append(new_dic)
        all_dic.extend(new_dic)



n=int(input())
dictionary=input().split()
string=input()
check(string,dictionary)
