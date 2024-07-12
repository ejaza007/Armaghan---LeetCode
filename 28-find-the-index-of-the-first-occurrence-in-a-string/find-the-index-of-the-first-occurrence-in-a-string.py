class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1

        nlen = len(needle)

        for i in range(len(haystack)):
            word = haystack[i:len(needle) + i]
            if word == needle:
                return i
        return -1 





