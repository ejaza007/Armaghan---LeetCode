class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        countMap = {0: 1}  # Initialize with 0:1 to handle subarrays that start from the beginning
        add = 0

        for num in nums:
            add += num
            if add - k in countMap:
                res += countMap[add - k]
            if add in countMap:
                countMap[add] += 1
            else:
                countMap[add] = 1
                
        return res



        