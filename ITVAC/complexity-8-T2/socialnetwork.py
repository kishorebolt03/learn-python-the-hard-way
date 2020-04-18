'''
In a social network, a person can invite friends of his/her friend. John wants to invite and add new friends. Complete the program below so that it prints the names of the persons to whom John can send a friend request.
'''

s={}
for i in range(int(input())):
	S=input().split()
	s[S[0]]=S[2:]
for i in s.values():
	for j in i:
		if j not in s.keys():
			print(j,end=' ')
