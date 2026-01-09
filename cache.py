"""
caching system (Memoization)
Goal: Cache the result of expensive function calls (like Fibonacci)so repeated calls are faster.
Memoization : is like keeping a register of  previous answers so the system doesnt repeat expensive work
"""
def decorator(func):
    cache = {}
    def wrapper(*args,**kwargs):
        if args in cache:
            return cache[args]
        print(f"calculating{args}")
        result = func(*args,**kwargs)
        cache[args] = result
        return result
    return wrapper

@decorator
def fibonaccie(n):
    if n <=1:
        return n
    return fibonaccie(n-1)+fibonaccie(n-2)

print(fibonaccie(10))
print(fibonaccie(2))
print(fibonaccie(10))