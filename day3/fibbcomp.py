def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

fib_gen = (num for num in fibonacci(10) )

print(list(fib_gen))