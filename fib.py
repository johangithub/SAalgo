from time import time

# recursive
def fib(n):
    if n<=2:
        return 1
    else:
        return fib(n-2) + fib(n-1)

# top-down memoization
memo = {}
memo[1] = 1
memo[2] = 1
def fib_memo(n):
    if n in memo:
        return memo[n]
    memo[n] = fib_memo(n-2) + fib_memo(n-1)
    return memo[n]

# bottom-up dynamic programming
def fib_dp(n):
    fib = [0] * (n+1)
    fib[1] = 1
    fib[2] = 1
    if n<=2:
        return fib[n]
    for i in range(3,n+1):
        fib[i] = fib[i-2] + fib[i-1]
    return fib[n]

n=
1#2 start_1 = time()
# print("First Fib: {}".format(fib(n)))
# print("Done in {} seconds".format(time()-start_1))

start_2 = time()
print("Second Fib: {}".format(fib_memo(n)))
print("Done in {} seconds".format(time()-start_2))

start_3 = time()
print("Third Fib: {}".format(fib_dp(n)))
print("Done in {} seconds".format(time()-start_3))

