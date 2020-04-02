# #!/bin/python3
#
# import math
# import os
# import random
# import re
# import sys
# from bisect import bisect_left
#
# # Complete the climbingLeaderboard function below.
# def rBs(aList, target, start, end):
#     midpoint = start + (end-start) // 2
#     #print(midpoint)
#     if aList[midpoint] == target:
#         return midpoint
#     elif target > aList[midpoint]:
#         return rBs(aList, target, start, midpoint)
#     else:
#         return rBs(aList ,target, midpoint+1, end)
#
# def climbingLeaderboard(scores, alice):
#     # print(scores,alice)
#     for i in alice:
#         scores.append(i)
#         scores = sorted(list(set(scores)),reverse=True)
#         yield abs(rBs(list(scores),i,0,len(list(scores)))+1)
#
#
#
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     scores_count = int(input())
#
#     scores = list(map(int, input().rstrip().split()))
#
#     alice_count = int(input())
#
#     alice = list(map(int, input().rstrip().split()))
#
#     result = climbingLeaderboard(scores, alice)
#
#     fptr.write('\n'.join(map(str, result)))
#     fptr.write('\n')
#
#     fptr.close()



#!/bin/python3

n = int(input().strip())
scores = list(reversed(sorted(list(set([int(scores_temp) for scores_temp in input().strip().split(' ')])))))
m = int(input().strip())
alice = [int(alice_temp) for alice_temp in input().strip().split(' ')]

for x in alice:
    while len(scores) > 0 and scores[-1] <= x:
        del scores[-1]
    print(len(scores) + 1)
