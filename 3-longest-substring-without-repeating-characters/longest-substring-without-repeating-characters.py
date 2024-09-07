class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        res = 0
        l, r = 0, 0

        while r < len(s):
            if s[r] not in charSet:
                charSet.add(s[r])
                r += 1
                res = max(res, r - l)
            else:
                while s[r] in charSet and l < r:
                    charSet.remove(s[l])
                    l += 1
        return res
