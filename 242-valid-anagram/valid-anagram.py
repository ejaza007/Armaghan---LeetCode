class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        smap = {}
        tmap = {}

        for char in s:
            if char in smap:
                smap[char] +=1
            else:
                smap[char] = 1
        

        for char in t:
            if char in tmap:
                tmap[char] +=1
            else:
                tmap[char] = 1
        
        return smap == tmap


        
        
        