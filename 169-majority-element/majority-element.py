class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        n = len(nums) // 2
        numMap = {}

        for num in nums:
            numMap[num] = 1 + numMap.get(num,0 )
            if numMap[num] > n:
                return num
        return -1
        
        