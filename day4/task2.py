# factorial using recursion

def fact(num):
    if not num or num == 1:
        return num
    return num * fact(num-1)

print(fact(5))