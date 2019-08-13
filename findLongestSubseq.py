# write a function that takes two strings, s1 and s2
# and returns the longest common subsequence of s1 and s2
# 
# "ABAZDC", "BACBAD" => "ABAD"
# "AGGTAB", "GXTXAYB" => "GTAB"
# "aaaa", "aa" => "aa"

# "ABAZDC", "BACBAD" => "ABAD"

# s1 = "ABAZDC"
# longestStr = 'ABAD'
# tempStr = ''
# s2 = ""
# temp


def longestSubseq(s1: str, s2: str) -> str:
    longestStr = ''
    lStr, sStr = max(s1, s2), min(s1, s2)
#     last index of occurence
    for i in range(len(sStr)):
        tempStr = longestSubseqHelper(sStr[i], sStr[i+1:], lStr, '')
        if len(tempStr) > len(longestStr):
            longestStr = tempStr
    return longestStr

def longestSubseqHelper(current: str, s1: str, s2: str, tempStr: str) -> str:
    if not s2:
        return tempStr
    else:
        if current in s2:
            tempStr += current
            if not s1:
                return tempStr
            currentIndex = s2.index(current)
            return longestSubseqHelper(s1[0], s1[1:], s2[currentIndex+1:], tempStr)
        else:
            t = s1[1:]
            return longestSubseqHelper(s1[0], s1[1:], s2, tempStr)

# print(lcs('AGGTAB', 'GXTXAYB'))
def lcsTest():
    assert(longestSubseq('', 'aaaa')) == '', 'something went wrong'
    assert(longestSubseq('ABAZDC', 'BACBAD')) == 'ABAD', 'something went wrong'
    assert(longestSubseq('AGGTAB', 'GXTXAYB')) == 'GTAB', 'something went wrong'
    assert(longestSubseq('aaaa', 'aa')) == 'aa', 'something went wrong'
    

lcsTest()
print('lcs passed!')