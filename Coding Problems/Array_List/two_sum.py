from numpy import indices


def tow_sum(nums,target):
    seen={}
    for i,num in enumerate(nums):
        complement=target-num
        if complement in seen:
            return [seen[complement],i]
        seen[num]=i
nums=[2,7,11,15]
target=9
indix=tow_sum(nums,target)
print(f"Indices of the number are :{indix}")