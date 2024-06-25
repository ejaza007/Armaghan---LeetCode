from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')
        res = 0

        for i in range(len(nums) - 2):  # Ensure there are at least two more elements after nums[i]
            l, r = i + 1, len(nums) - 1

            while l < r:
                threesum = nums[i] + nums[l] + nums[r]

                if abs(threesum - target) < abs(closest):
                    closest = threesum - target
                    res = threesum

                if threesum > target:
                    r -= 1
                elif threesum < target:
                    l += 1
                else:
                    return threesum
        
        return res

    




        