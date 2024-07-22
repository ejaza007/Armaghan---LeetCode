from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        slow = 2  # Start from the third element since the first two can be duplicates
        for fast in range(2, len(nums)):
            if nums[fast] != nums[slow - 2]:  # Compare with the element two positions back
                nums[slow] = nums[fast]
                slow += 1
        
        return slow

    






     #  l = 1  # Pointer to place the next unique element

        #for r in range(1, len(nums)):
            #if nums[r] != nums[r - 1]:
             #   nums[l] = nums[r]
              #  l += 1

        #return l
        