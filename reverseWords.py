class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        tmpStr = ''
        tmpLst = []
        for i, char in enumerate(s):
            if i == len(s) - 1:
                tmpStr += char            
                tmpLst.append(tmpStr)
            if char == ' ':
                tmpLst.append(tmpStr)
                tmpStr = ''
            else:
                tmpStr += char
        tmpLst = tmpLst[::-1]
        resultLst = []
        for i, v in enumerate(tmpLst):
            resultLst += [char for char in v]
            resultLst.append(' ')
        resultLst.pop()
        s = resultLst
        # s = "the sky is blue".split()
        # s = reversed(s)
        # print([word + " " for word in s])
        # print([j for j in reversed([1,2,3])])
        # # print("".join( [word+" " for word in reversed("the sky is blue".split()) ] ))