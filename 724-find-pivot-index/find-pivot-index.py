class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = [0] * len(nums)
        rightSum = [0] * len(nums)
        lefter = 0
        righter = 0

        for i in range(len(nums)):
            leftSum[i] = lefter
            lefter+=nums[i]
        for i in range(len(nums) - 1, -1, -1):
            rightSum[i] = righter
            righter+=nums[i]
        
        for i in range(len(nums)):
            if rightSum[i] == leftSum[i]:
                return i
        return -1
        

        