class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        addMap = {}
        for i in range(len(nums)):
            if target - nums[i] in addMap:
                return [i,addMap[target - nums[i]]]
            else:
                addMap[nums[i]] = i
        return [-1,-1]

        