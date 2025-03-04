# fibonacci using recursion

def fib_itr(n):
    if n == 0:
        print(n)
    if n == 1:
        print(1)
    elif n == 2:
        print([0, 1])
    A = [0] * n
    A[1] = 1
    for i in range(2, n):
        A[i] = A[i-1] + A[i-2]
    print(A)

def fib_rec(n):
    if not n or n == 1:
        return n
    return fib_rec(n-1) + fib_rec(n-2)

n = int(input())
for i in range(n):
    print(fib_rec(i), end=' ')