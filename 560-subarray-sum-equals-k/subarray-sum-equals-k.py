class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        summap = {0: 1}  # Initialize with 0:1 to handle subarrays starting from index 0
        total = 0

        for num in nums:
            total += num  # Add current num to the running total
            if total - k in summap:
                res += summap[total - k]  # Add the count of subarrays that sum to k
            summap[total] = summap.get(total, 0) + 1  # Update the count of the current total in summap

        return res

        