from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zero, one = 0, 0
        res = 0
        diffIndex = {0: -1}

        for i in range(len(nums)):
            if nums[i] == 0:
                zero += 1
            else:
                one += 1
            
            diff = one - zero
            
            if diff in diffIndex:
                res = max(res, i - diffIndex[diff])
            else:
                diffIndex[diff] = i
        
        return res







        