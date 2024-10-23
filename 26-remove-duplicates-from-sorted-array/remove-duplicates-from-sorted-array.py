class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        # `k` starts at 1 because the first element is always valid in the sorted array
        k = 1
        
        for i in range(1, len(nums)):
            # Check if the current element is different from the previous one
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1
        
        return k
