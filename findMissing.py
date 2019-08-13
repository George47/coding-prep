def reverse(s:str) -> str:
    return s[::-1]


def reverseIter(s: str) -> str:
    s = list(s)
    for i in range(int(len(s)/2)):
        s[i], s[-i-1] = s[-i-1], s[i]
    return ''.join(s)
        
def findMissing(a1: list, a2: list) -> int:
    lLst = max(a1, a2)
    sLst = min(a1, a2)
    newLst = []
    for i in range(max(len(a1), len(a2))):
        if lLst[i] not in sLst:
            newLst.append(lLst[i])
    return newLst

    
    # return s

def findMissingTest():
    assert(findMissing([4, 8, 12, 9, 3, 15, 51], [4, 8 ,9 ,3])) == 2, 'something went wrong'


if __name__ == '__main__':
    findMissingTest()
    print('Test cases passed')