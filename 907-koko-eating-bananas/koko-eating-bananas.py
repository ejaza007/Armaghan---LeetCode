class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        k = max(piles)


        while l<=r :
            mid = (l + r) // 2
            adder = 0

            for p in piles:
                adder += math.ceil(p/mid)
            if adder <= h:
                k = mid
                r = mid - 1
            else:
                l = mid + 1
        return k
      
        



        