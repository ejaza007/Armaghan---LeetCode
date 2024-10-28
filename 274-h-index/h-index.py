from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        res = 0

        for i, h in enumerate(citations):
            if h >= len(citations) - i:
                res = len(citations) - i
                break  # We found the h-index, so we can exit the loop

        return res
