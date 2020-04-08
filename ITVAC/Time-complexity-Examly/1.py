'''
Given a string S, print the minimum number of characters you have to remove from the string S to make it a clean string. A clean string is a string in which all the characters are distinct.

Input:
First line of input contains a string S, (1≤|S|≤10000)
. S consists of lowercase characters only.
Output:

Print an integer denoting the minimum number of characters you have to remove from S to make it a good string.

Need the most efficient algorithm since the problem is tagged with timelimit of 100 ms.
'''
s=list(input())
S=set(s)
print(len(s)-len(S))
