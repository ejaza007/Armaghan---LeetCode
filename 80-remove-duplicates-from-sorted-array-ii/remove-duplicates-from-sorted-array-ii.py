class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)  # If the list has 2 or fewer elements, no need to modify
        
        # Start the pointer at index 2
        k = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1
        
        return k  # Return the length of the modified array
