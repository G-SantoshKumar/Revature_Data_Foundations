lst = [1,2,3,3,2,2,5,7]
def remove_duplicates_new(nums):
    seen = set()
    distinct = []
    for num in nums:
        if num not in distinct:
            distinct.append(num)
        else:
            seen.add(num)
    return distinct, seen

print(remove_duplicates_new(lst))