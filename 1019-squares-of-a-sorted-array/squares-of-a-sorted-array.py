class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l,r = 0 ,len(nums) - 1
        res = [0] * len(nums)
        pos = r

        while l<=r:
            lsq , rsq = nums[l] * nums[l], nums[r] * nums[r]
            if lsq >rsq:
                res[pos] = lsq
                l+=1
            else:
                res[pos] = rsq
                r-=1
            pos -=1
        return res         