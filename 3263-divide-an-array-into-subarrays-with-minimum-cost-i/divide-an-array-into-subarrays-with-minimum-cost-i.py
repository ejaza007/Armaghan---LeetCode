class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        min1, min2 = float('inf'), float('inf')
        cost = nums[0]

        for i in range(1,len(nums)):
            if nums[i] < min1:
                min2 = min1
                min1 = nums[i]
            elif nums[i] < min2:
                min2 = nums[i]
        cost =  cost + min1 + min2
        return cost
        