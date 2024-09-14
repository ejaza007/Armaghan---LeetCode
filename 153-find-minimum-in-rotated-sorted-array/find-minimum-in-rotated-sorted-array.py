from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        # If the array is not rotated (already sorted), return the first element
        if nums[l] < nums[r]:
            return nums[l]

        while l < r:
            mid = (l + r) // 2

            # If mid element is greater than the rightmost element, the pivot is in the right half
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                # If the mid element is less than or equal to the rightmost element, the pivot is in the left half
                r = mid

        # When l == r, we found the pivot point, which is the smallest element
        return nums[l]

        