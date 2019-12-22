n=int(input())
if n<=5 or n>50:
        print("No Pattern")
else:
	for i in range(n):
		for j in range(n-2):
			if ((i==0) and j>0) or(i==(n//2)-1 and j>1 and j<n-3) or (i==n-1 and j<n-3 and j>0) or (j==0 and i>0 and i<n-1) or (j==n-3 and i>=(n//2)-1 and i<n-1):
				print("*",end='')
			else:
				print(end=' ')

		print()
