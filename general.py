class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
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

    def wiggleSort(self, nums: List[int]) -> None:
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
