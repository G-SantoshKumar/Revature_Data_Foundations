def second_largest(numbers):
    return sorted(set(numbers))[-2]


lst = [-800, -6, 2, 8, 7, 1, 1, 60]
print(second_largest(lst))