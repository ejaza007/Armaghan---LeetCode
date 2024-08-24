class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counted = Counter(nums)

        heap = []

        for num, freq in counted.items():
            heapq.heappush(heap, (freq, num))
            
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []

        for freq,num in heap:
            res.append(num)

        return res

        