def twoSum(nums, target):
    dic = {}
    for i, j in enumerate(nums):
        if target-j in dic:
            return dic[target-j], i
        dic[j] = i
    return None