from functools import cache
def fib_mem(n, memo = {}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_mem(n-1, memo) + fib_mem(n-2, memo)
    return memo[n]

print(fib_mem(10))
print(fib_mem(50))


@cache
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(10))
print(fib(50))
