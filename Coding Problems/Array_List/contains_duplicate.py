def contains_duplicate(nums):
    s=set(nums)
    ns=len(s)
    nl=len(nums)
    if ns==nl:
        return "There is no duplicate"
    else:
        return "There is duplicates"

print(contains_duplicate([1,2,3,1]))

                     #OR
def Contains_duplicate(nums):
    seen=set()
    for num in nums:
        if num in seen:
            return "There is duplicates"
        seen.add(num)
    return "There is no duplicates"

nums=[1,2,3,4,5,6,7,8,9]
print(contains_duplicate(nums))