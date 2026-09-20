class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        elem = 0
        contador = 0
        for numero in nums:
            if contador == 0:
                elem = numero
                contador += 1
            elif elem == numero:
                contador += 1
            else:
                contador -= 1
        
        return elem