class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        countFirst = Counter(s1)
        countSecond = Counter(s2[:len(s1)])

        if countFirst == countSecond:
            return True
        
        l = 0

        for r in range(len(s1), len(s2)):
            countSecond[s2[l]] -=1

            if countSecond[s2[l]] == 0:
                del countSecond[s2[l]]

            countSecond[s2[r]] = countSecond.get(s2[r], 0) + 1

            if countSecond == countFirst:
                return True
            l+=1
        return False
            

            




        