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

def simplify(Str): 
    Len = len(Str) 
  
    # resultant String of max Length 
    # equal to Length of input String  
    res = [''] * Len
    index = 0
    i = 0
  
    # create empty stack  
    s = [] 
    s.append(0)  
  
    while (i < Len):  
        # if sign, flip based on stack space
        if (Str[i] == '+'):  
  
            # If top is 1, flip the operator  
            if (s[-1] == 1):  
                res[index] = '-'
                index += 1
  
            # If top is 0, append the  
            # same operator  
            if (s[-1] == 0): 
                res[index] = '+'
                index += 1
  
        # same for - sign, 
        elif (Str[i] == '-'): 
            if (s[-1] == 1):  
                res[index] = '+'
                index += 1
            elif (s[-1] == 0):  
                res[index] = '-'
                index += 1

        # checking if its (
        elif (Str[i] == '(' and i > 0): 
            if (Str[i - 1] == '-'): 
  
                # x is opposite to the top of stack  
                x = 0 if (s[-1] == 1) else 1
                s.append(x) 
  
            # append value equal to top of the stack  
            elif (Str[i - 1] == '+'):  
                s.append(s[-1]) 
  
        # If closing parentheses pop 
        # the stack once  
        elif (Str[i] == ')'):  
            s.pop()  
  
        # copy the character to the result  
        else: 
            res[index] = Str[i] 
            index += 1
        i += 1
    return ''.join(res) 

def checkValidString(s: str) -> bool:
        if not s:
            return True
        stack = []
        for v in s:
            if v == '(' or v == '*':
                stack.append(v)
            elif v == ')':
                if not stack:
                        return False
                if stack[-1] == '(' or stack[-1] == '*':
                    stack.pop()
                else:
                    return False
        return True

def minMoves2(nums):
    d = {}
    for num in nums:
        if num in d:
            d[num] += 1
        else:
            d[num] = 0
    return sorted(d)

def maxIsland(grid):
    def dfs(row, col, grid, size):
        if row < 0 or col < 0 or row == len(grid) or col == len(grid[0]) or grid[row][col] != '1':
            return 0
        else:
            grid[row][col] = '0'
            return 1 + dfs(row + 1, col, grid, size) + dfs(row - 1, col, grid, size) + dfs(row, col + 1, grid, size) + dfs(row, col - 1, grid, size)
    
    maxIsland = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '1':
                size2 = dfs(row, col, grid, 0)
                maxIsland = max(maxIsland, size2)
    return maxIsland

def expand(S: str):
    def parse(S):
        result = []
        r = None
        for x in S:
            if x == '{':
                r = []
            elif x == ',':
                continue
            elif x == '}':
                result.append(sorted(r))
                r = None
            elif r == None:
                result.append([x])
            else:
                r.append(x)
        return result

    p = parse(S)
    result = []

    def dfs(p, i, r=[]):
        if i == len(p):
            result.append(''.join(r))
            return
        for x in p[i]:
            r.append(x)
            dfs(p, i+1, r)
            r.pop()
    dfs(p,0)
    return result

def simplifyEquation(s: str) -> str:
    # cases to consider
    # if current is - and next is (
    # means need to flip sign
    triggerCounter = 0
    stack = []
    result = ''
    for i in range(len(s)):
        # if -( then need to trigger
        if s[i] == '-' and s[i+1] == '(':
            triggerCounter += 1
            stack.append('-(')
            sign = s[i]
            for j in range(triggerCounter - 1):
                sign = flipSign(sign)
            result += sign
            continue
        # when encountering closing bracket
        if s[i] == ')':
            if stack.pop() == '-(':
                triggerCounter -= 1
        if s[i] in ['(', ')']:
            continue
        if s[i] in ['+', '-']:
            sign = s[i]
            for z in range(triggerCounter):
                sign = flipSign(sign)
            result += sign
            continue
        result += s[i]
    return result

def flipSign(sign: str) -> str:
    signs = {
        '+': '-',
        '-': '+'
    }
    return signs[sign]

def simplifyChars(s: str) -> str:
    # 2 cases,
    # digit
    #   record digit, record i+1 char
    #   push both onto stack
    # char
    #   if last in stack is same, += 1
    #   else push onto stack
    charStack = []
    countStack = []
    i = 0
    result = ''
    count = 0
    # using while loop to increment the index
    while i <= len(s) - 1:
        # digit case
        if s[i].isdigit():
            count = int(s[i])
            # check for multiple digits and save them as integer 
            while s[i+1].isdigit():
                count += int(s[i+1])
                i += 1
            # if stack doesnt exist or last element is not i, push to stacks
            if not charStack or charStack[-1] != s[i+1]:
                countStack.append(count)
                charStack.append(s[i+1])
            # if stack exists, push the count and char to stack
            else:
                toInt = int(countStack[-1]) + int(s[i])
                countStack[-1] = toInt 
            # inc the index
            i += 1
        # non-digit case
        # same as digit case but treat as digit = 1
        else:
            if not charStack or charStack[-1] != s[i]:
                charStack.append(s[i])
                countStack.append(1)
            else:
                toInt = int(countStack[-1]) + 1
                countStack[-1] = toInt
        i += 1
    
    # add the stacks to result str
    for j in range(len(charStack)):
        if int(countStack[j]) > 1:
            result += str(countStack[j])
        result += charStack[j]
    return result

if __name__ == '__main__':
    # print(expand('{a,b}c{d,e}f'))
    # print(simplifyEquation('-(a+b)+a'))
    # print(simplify('-(a-(b-c-(d+e))-f)'))
    # print(simplifyEquation('-(a-(b-c-(d+e))-f)'))
    # # a-(b-c-(d+e))-f => a-b+c-d+e-f
    # s = 'test'
    # dic = {}
    # for char in s:
    #     dic[char] = dic.get(char, 0) + 1
    # print(dic)

    print(simplifyChars('99a2a5b'))
    print(simplifyChars('9a2b5a'))
    print(simplifyChars('a111abbccddee'))
    print(simplifyChars(''))
    print(simplifyChars('5ab3bccd1dee'))

    # print(checkValidString('(()'))
    # print(wordPattern('abba', 'dog dog dog dog'))
    # print(simplify('a-(b-c-(d+e))-f'))
    # print(convertEquation('-(a+b)'))
    # print(findLengthOfLCISImprove([1,3,5,4,7]))
    # print(findLengthOfLCISImprove([2,2,2,2,2]))
    # print(findLengthOfLCISImprove([]))
    # print(findLengthOfLCISImprove([1,3,5,7]))

    # print(reverseStr('abcdefg', 2))
    # print(containsDuplicate([1,2,3,4,5]))

    # # print(convertToBase7(-7))

    # print(sum([1,23]))
    # print(maxIsland([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]))
