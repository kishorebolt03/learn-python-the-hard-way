def rec(arr,i,j,s):
	if j==i+1:
		return max(arr[i],arr[j])
	return max((s-rec(arr,i+1,j,s-arr[i])),(s-rec(arr,i,j-1,s-arr[j])))

for i in range(int(input())):
	n=int(input())
	arr=list(map(int,input().split()[:n]))
	print(rec(arr,0,len(arr)-1,sum(arr)))