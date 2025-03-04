def closest_to_zero(lst):
    return min(lst, key=lambda x: (abs(x), -x))  

nums = [-4, 2, -1, 3, -2]
print(closest_to_zero(nums)) 