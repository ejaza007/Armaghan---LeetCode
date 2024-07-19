from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)  # Sort the array in non-increasing order
        
        # Iterate through the array to find the largest perimeter
        for i in range(len(nums) - 2):
            if nums[i] < nums[i + 1] + nums[i + 2]:
                return nums[i] + nums[i + 1] + nums[i + 2]
        
        return 0  # Return 0 if no valid triangle can be formed

# Example usage:
solution = Solution()
print(solution.largestPerimeter([2, 1, 2]))  # Output: 5
print(solution.largestPerimeter([1, 2, 1]))  # Output: 0
print(solution.largestPerimeter([3, 2, 3, 4]))  # Output: 10
print(solution.largestPerimeter([3, 6, 2, 3]))  # Output: 8
