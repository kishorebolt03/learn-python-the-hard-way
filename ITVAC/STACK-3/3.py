'''
Waiter

You are a waiter at a party. There are N stacked plates on pile A0. Each plate has a number written on it.Then there will be Q iterations. In i-th iteration, you start picking up the plates in Ai-1 from the top one by one and check whether the number written on the plate is divisible by the i-th prime. If the number is divisible, you stack that plate on pile Bi. Otherwise, you stack that plate on pile Ai. After Q iterations,plates can only be on pile B1,,B2.........BQ,AQ. Output numbers on these plates from top to bottom of 

each piles in order of B1,,B2.........BQ,AQ.



Note:

The first line contains two space separated integers N, and Q.
The next N line contains space separated integers representing the initial pile of plates, i.e.,A0 . The leftmost value represents the bottom plate of the pile.
Output N lines. Each line contains a number written on the plate. Printing should be done in the order defined above.



'''

generated_primes = [...]
 
def solveWaiter(N, Q, numbers):
    stack = []
     
    for value in numbers:
        if value % generated_primes[0] != 0:
            stack.append(value)
        else:
            print value
     
     
    for prime_idx in xrange(1, Q):
        leftover = []
         
        while stack:
            value = stack.pop()
            if value % generated_primes[prime_idx] != 0:
                leftover.append(value)
            else:
                print value
        stack = leftover
     
    for value in stack:
        print value
 
def main():
    N, Q = map(int, raw_input().split())
     
    numbers = map(int, raw_input().split())
     
    solveWaiter(N, Q, numbers)
     
 
if __name__ == '__main__':
    main()