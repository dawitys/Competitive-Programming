def fib(n):
    f0 = 0
    f1 = 1
    for i in range(n-1):
        f = f0 + f1
        f0 = f1
        f1 = f
    return f1

print(fib(3))