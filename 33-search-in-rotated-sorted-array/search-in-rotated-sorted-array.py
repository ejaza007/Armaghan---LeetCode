from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            
            # Check if the target is found
            if nums[m] == target:
                return m
            
            # Check if the left side is sorted
            if nums[l] <= nums[m]:
                # Target is in the left sorted part
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # The right side is sorted
            else:
                # Target is in the right sorted part
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1  # Return -1 if target is not found


        