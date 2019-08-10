# Given string like "-(a+b) + c - (d-e)" convert it to an equivalent equation without the brackets.  
def convertEquation(equation):
    trigger = False
    result = ''
    length = len(equation)

    # if 
    # print(equation[222])
    
    for key, val in enumerate(equation):
        # if (key < length && trigger):
        if not val or val == '(':
            continue

        if val == '-':
            if equation[key + 1] == '(' or equation[key + 2] == '(':
            # improvements, detect future cases
                trigger = True
                result += val
                continue

        if val == ')':
            trigger = False
            continue

        if trigger == True and val in ['+', '-']:
            val = reverse(val)
        
        result += val
        
    return result

def reverse(sign):
    switcher = {
        '+': '-',
        '-': '+',
        True: False,
        False: True
    }
    return switcher[sign]

def testCases():
    assert convertEquation("-(a+b) + c - (d-e)") == "-a-b + c - d+e", "should be -a-b + c - d+e"


# if current is -, and next is (, then set trigger true,
# if trigger true, convert + and - to opposite
# 

    # return result


# Finding smallest int in array
def findMin(arr):
    currentMin = arr[0]
    for n in arr:
        if n <= currentMin:
            currentMin = n
    return currentMin

def findSecondMin(arr):
    currentMin = arr[0]
    currentMin2 = arr[1]
    for n in arr:
        if n < currentMin:
            currentMin2 = currentMin
            currentMin = n
        elif n < currentMin2:
            currentMin2 = n
        
    return currentMin2

def findNthSmallest(n, arr):
    for key, value in enumerate(arr):
        print(key, value)

def reversee(str):
    newStr = ''
    for v in str:
        newStr = v + newStr
    print(newStr)

def findMinTest():
    assert(findMin([5,4,3,2,1])) == 1, 'should be 1'
    assert(findMin([5,13,512,3,5,23,6,8])) == 3, 'should be 3'
    assert(findSecondMin([5,4,3,2,1])) == 2, 'should be 2'
    assert(findSecondMin([7,13,512,3,5,23,6,8])) == 5, 'should be 5'

if __name__ == '__main__':
    # print(convertEquation("-(a+b) + c - (d-e)"))
    # test cases 
    # testCases()
    # print("all test cases good")
    reverse('hello')
    findNthSmallest(1, [1,2,3])
    findMinTest()
    print('test cases complete')