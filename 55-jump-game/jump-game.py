class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxR = 0
        for i, length in enumerate(nums):
            if i > maxR:
                return False
            maxR = max(maxR, i + length)
        return True

        