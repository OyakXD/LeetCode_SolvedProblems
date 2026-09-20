class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        indices = []
        
        for x in range(len(nums)):
            for y in range(x+1, len(nums)):
                if (nums[x] + nums[y]) == target:
                    indices.append(x)
                    indices.append(y)
                    return indices

        