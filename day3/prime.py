def is_prime(x):
    if x < 2:  # 0 and 1 are not prime
        return False
    ct = 0
    for i in range(1, x + 1):
        if x % i == 0:
            ct += 1
    return ct == 2  # A prime number has exactly two divisors

print(set(x for x in range(1, 51) if is_prime(x)))
