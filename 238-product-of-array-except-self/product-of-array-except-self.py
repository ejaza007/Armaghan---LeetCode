class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preres = [1] * len(nums)
        postres = [1] * len(nums)
        res = [1] * len(nums)
        prefix = 1
        postfix = 1

        for i in range(len(preres)):
            preres[i] = prefix
            prefix *= nums[i]
        
      
        for i in range(len(nums) - 1, -1, -1):
            postres[i] = postfix
            postfix *= nums[i]
        
        for i in range(len(nums)):
            res[i] = postres[i] * preres[i]

        return res



        