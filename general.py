def findStrobogrammatic(n):
    # rotate exactly 180 still remains the same
    # n = 2 => 11, 69, 88, 96
    # n = 3 => 111, 888 
    # n = 4 => 1111, 6969, 8888, 9696
    # n = 5 => 11111, 88888
    def gen(n, outermost):
        if n == 0: return [""]
        elif n == 1: return ["0", "1", "8"]
        
        middles = gen(n-2, outermost=False)
        res = []
        for mid in middles:
            if not outermost:
                res.append("0" + mid + "0")
            res.append("1" + mid + "1")
            res.append("8" + mid + "8")
            res.append("6" + mid + "9")
            res.append("9" + mid + "6")
        return res
            
    return gen(n, outermost=True)

def wiggleSort(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # trigger: True for <=, Flase for >=
    trigger = True
    for i in range(len(nums) - 1):
        if trigger:
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
        else:
            if nums[i] < nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
        trigger = not trigger

# 48. Rotate Image
def rotate(matrix) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix[0])
    for i in range(n // 2 + n % 2):
        for j in range(n // 2):
            tmp = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
            matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]
            matrix[j][n - 1 - i] = matrix[i][j]
            matrix[i][j] = tmp
            
def findLengthOfLCIS(nums) -> int:
    if not nums:
        return 0
    maxCount = 1
    for i in range(len(nums) - 1):
        count = 1
        z = i
        while z < len(nums) - 1:
            if nums[z] < nums[z+1]:
                count += 1
            else:
                break
            z += 1
        maxCount = max(maxCount, count)
    return maxCount

def findLengthOfLCISImprove(nums) -> int:
    if not nums:
        return 0
    
    newArr = []
    for i in range(len(nums) - 1):
        tmpArr = []
        # if nums[i] < nums[i+1]

def reverseStr(s, k):
    if len(s) < k:
        return s[::-1]
    tmpLst = list(s[k:])
    tmpLst2 = list(s[:k])
    return "".join(tmpLst2 + tmpLst)
    # print(tmpLst2, tmpLst)

def containsDuplicate(nums):
    for i in range(1, len(nums)):
        print(nums[:i], nums[i:])

def convertToBase7(num: int) -> str:
        r = str(num % 7)
        print(r)
        if num // 7 == 0:
            return r
        else:
            return r + convertToBase7(num // 7)

def convertEquation(s: str) -> str:
    for char in s:
        print(char)

def wordPattern(pattern: str, str: str) -> bool:
    dictionary = str.split()
    taken = []
    if len(pattern) != len(dictionary):
        return False
    refDict = {}
    for i in range(len(pattern)):
        if dictionary[i] in taken:
            if pattern[i] not in refDict or dictionary[i] != refDict[pattern[i]]:
                return False

        if pattern[i] not in refDict:
            refDict[pattern[i]] = dictionary[i]
            taken.append(dictionary[i])
        else:
            if refDict[pattern[i]] != dictionary[i]:
                return False
    print(taken)
    return True

if __name__ == '__main__':
    print(wordPattern('abba', 'dog dog dog dog'))
    # print(convertEquation('-(a+b)'))
    # print(findLengthOfLCISImprove([1,3,5,4,7]))
    # print(findLengthOfLCISImprove([2,2,2,2,2]))
    # print(findLengthOfLCISImprove([]))
    # print(findLengthOfLCISImprove([1,3,5,7]))

    # print(reverseStr('abcdefg', 2))
    # print(containsDuplicate([1,2,3,4,5]))

    # # print(convertToBase7(-7))

    # print(sum([1,23]))