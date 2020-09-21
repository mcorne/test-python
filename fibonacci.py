def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    fib_1 = fib_2 = 1
    sum = 0
    for i in range(3, n+1):
        sum = fib_1 + fib_2
        fib_1, fib_2 = sum, fib_1
    return sum
    
for n in range(1, 10):    
    print(n, "->", fib(n))    