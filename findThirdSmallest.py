# a function to detect the third smallest number in a set of numbers
def findThirdSmallest(candidates: set) -> int:
    if len(candidates) < 3:
        return 0
    return sorted(candidates)[2]
# O(nlogn)

def findThirdSmallestImprove(candidates: set, n: int) -> int:
    candidates = list(candidates)
    candidatesLen = len(candidates)
    if n > candidatesLen:
        return 0
    for i in range(candidatesLen - 1):
        if candidates[i] > candidates[i+1]:
            candidates[i], candidates[i+1] = candidates[i+1], candidates[i]
    return candidates[n-1]
# O(n)
        
def findThirdSmallestIter(candidates: set) -> int:
    candidates = list(candidates)
    if len(candidates) == 3:
        return candidates[2]
    elif len(candidates) < 3:
        return 0

    shortCandidates = sorted(candidates[0:3])
    min1 = shortCandidates[0]
    min2 = shortCandidates[1]
    min3 = shortCandidates[2]
    
    for i in range(2, len(candidates)):
        if candidates[i] < min1:
            min3 = min2
            min2 = min1
            min1 = candidates[i]
        elif candidates[i] < min2:
            min3 = min2
            min2 = candidates[i]
        elif candidates[i] < min3:
            min3 = candidates[i]
    return min3

def findThirdSmallestTest():
    assert(findThirdSmallestIter({16,3,42,15,1,6,2,0})) == 2, 'something went wrong'
    
if __name__ == '__main__':
    findThirdSmallestTest()
    print('Test cases passed!')
