from typing import List
import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each element
        frequency = Counter(nums)
        
        # Step 2: Use a min-heap to keep track of top k elements
        min_heap = []
        
        for num, freq in frequency.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        # Step 3: Extract the elements from the heap
        top_k_frequent = [num for freq, num in min_heap]
        
        return top_k_frequent

# Example usage:
solution = Solution()
nums = [1,1,1,2,2,3]
k = 2
print(solution.topKFrequent(nums, k))  # Output: [1, 2]
