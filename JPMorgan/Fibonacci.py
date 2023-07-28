# if you completed this by DP, you may tell that using memoization can improve the results.

# 0, 1, 1, 2, 3, 5, 8, 13, 21, ….
def fib(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif (n == 1) or (n == 2):
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(4))
print(fib(9))


def Fibonacci(num):
    Flist = []
    for i in range(num):
        Flist.append(fib(i))
    return Flist

print(Fibonacci(6))


# Find the Minimum Number of Fibonacci Numbers Whose Sum Is K:
def minFib(K):
    r=0
    while fib(r) < K:
        r += 1
    return len(Fibonacci(r))

print(minFib(7))


# Length of Longest Fibonacci Subsequence in an array