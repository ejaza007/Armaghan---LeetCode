from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
       
        l = 1  # Pointer to place the next unique element

        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1

        return l

# Test case
nums = [1, 1, 2]
solution = Solution()
length = solution.removeDuplicates(nums)
print(length)  # Output: 2
print(nums[:length])  # Output: [1, 2]
