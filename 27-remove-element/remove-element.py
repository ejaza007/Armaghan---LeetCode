from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Removes all instances of val in nums in-place and returns the new length.
        The order of elements can be changed. It doesn't matter what is left beyond the new length.
        """
        # Pointer to track position of the next element to keep
        k = 0

        # Iterate through all elements in the array
        for i in range(len(nums)):
            # If the current element is not equal to val, we keep it
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        # Return the length of the array after removal
        return k
