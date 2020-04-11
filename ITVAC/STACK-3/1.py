'''
Mancunian And Fantabulous Pairs

An array of length at least 2 having distinct integers is said to be fantabulous if the second highest element lies strictly to the left of the highest value.

Example, [1, 2, 13, 10, 15] is fantabulous as the second-highest value 13 lies to the left of highest value 15.

For every fantabulous array, we define a fantabulous pair (a, b) where a denotes the index of the second-highest value (1-indexed) and b denotes the index of the highest value (1-indexed). In the above array, the fantabulous pair is (3, 5).

Mancunian challenges you to solve the following problem.

Given an array, find the total number of distinct fantabulous pairs over all its subarrays.



Note:

The first line contains an integer N denoting the length of the array.

The next line contains N distinct integers denoting the elements of the array.

Output a single integer which is the answer to the problem.



Constraints:

1 <= N <= 106

1 <= array elements <= 109

Array elements are distinct.

Example:

arr=[1,2,3,4]

Explanation

Let us consider all the subarrays of the given array.

The subarray [1] is not fantabulous.

The subarray [2] is not fantabulous.

The subarray [3] is not fantabulous.

The subarray [4] is not fantabulous.

The fantabulous pair for subarray [1, 3] is (1, 2).

The subarray [3, 2] is not fantabulous.

The fantabulous pair for subarray [2, 4] is (1, 2).

The subarray [1, 3, 2] is not fantabulous.

The fantabulous pair for subarray [3, 2, 4] is (1, 3).

The fantabulous pair for subarray [1, 3, 2, 4] is (2, 4).

So, there are the 3 distinct pairs, which are (1, 2), (1, 3) and (2, 4).



'''

T = int(input())
L = list(map(int, input().split()))
dynamic = [-1] * T
stack = []
top = -1
for i in range(T):
    while top != -1 and L[stack[top]] < L[i]:
        dynamic[stack[top]] = i
        stack.pop()
        top -= 1
    if top == -1:
        stack.append(i)
        top += 1
    else:
        stack.append(i)
        top += 1
dynamic2 = [-1] * T
stack = []
top = -1
var = T - 1
while var != -1:
    while top != -1 and L[stack[top]] < L[var]:
        dynamic2[stack.pop()] = var
        top -= 1
    if top != -1:
        stack.append(var)
        top += 1
    else:
        stack.append(var)
        top += 1
    var -= 1
arr = [0] * T
for i in range(T):
    if dynamic[i] != -1:
        arr[dynamic[i] - i] = max([arr[dynamic[i] - i], i - dynamic2[i]])
print(sum(arr))