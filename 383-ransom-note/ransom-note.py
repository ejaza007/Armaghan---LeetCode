class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        magCount = Counter(magazine)

        for char in ransomNote:
            if char in magCount:
                magCount[char] -=1
                if magCount[char] == 0:
                    del magCount[char]
            else:
                return False
        return True
        