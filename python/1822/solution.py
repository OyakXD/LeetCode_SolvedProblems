class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        pro = 1
        for numeros in nums:
            pro *= numeros

        if pro > 0:
            return 1
        elif pro < 0:
            return -1
        return 0
    
        