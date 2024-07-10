class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numset = Counter(nums)

        for num in nums:
            if numset[num] > 1:
                return True
        return False