from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merges two sorted arrays into one sorted array in-place.
        Modifies nums1 to include elements from nums2.
        """
        # Start filling from the back of nums1
        length = m + n - 1
        i, j = m - 1, n - 1
        
        # Merge until nums2 is exhausted
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[length] = nums1[i]
                i -= 1
            else:
                nums1[length] = nums2[j]
                j -= 1
            length -= 1
