'''
You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.

Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c. Chain of pairs can be formed in this fashion.

Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. You can select pairs in any order.
'''

def findLongestChain(pairs):
    end, res = -1, 0
    pairs.sort(key=lambda p: p[1])
    for first, second in pairs:
        if end < first:
            end = second
            res += 1        
    return res

#driver
#get input and pass it to the function