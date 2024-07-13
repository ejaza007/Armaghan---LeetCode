class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()


        mapPW = {}
        mapWP = {}

        if len(pattern)!= len(words):
            return False
        for i in range(len(pattern)):
            c1,c2 = pattern[i], words[i]
            if ((c1 in mapPW and mapPW[c1] != c2) or (c2 in mapWP and mapWP[c2]!= c1)):
                return False
            mapPW[c1] = c2
            mapWP[c2] = c1
        return True


