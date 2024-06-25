class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        res = [1] * len(nums)
        preres = 1
        postres = 1


        for i in range(len(nums)):
            prefix[i] = preres
            preres = preres * nums[i]

        for i in range(len(nums) - 1,-1,-1):
            postfix[i] = postres
            postres = postres * nums[i]
            
        for i in range(len(nums)):
            res[i] = prefix[i] * postfix[i]
        
        return res

        



        
    

        