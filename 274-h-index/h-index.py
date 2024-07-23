class Solution:
    def hIndex(self, citations: List[int]) -> int:

        
        citations.sort()
        res = 0

        for i in range(len(citations)):   
            if len(citations) - i <= citations[i]:
                res = len(citations) - i
                break
                
        return res

        
            




        