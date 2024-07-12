from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            else:
                l += 1

        return l

# Test case
nums = [3, 2, 2, 3]
val = 3
solution = Solution()
length = solution.removeElement(nums, val)
print(length)  # Output: 2
print(nums[:length])  # Output: [2, 2]



        