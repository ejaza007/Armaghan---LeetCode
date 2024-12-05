class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        distinct_values = set(nums)
        distinct_values.discard(0)
        return len(distinct_values)