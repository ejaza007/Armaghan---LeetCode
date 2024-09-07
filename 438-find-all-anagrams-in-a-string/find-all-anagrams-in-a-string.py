from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        if len(p) > len(s):
            return []
        
        # Counter for pattern and for the first window in s
        p_counter = Counter(p)
        s_counter = Counter(s[:len(p)])

        # Check if the first window is an anagram
        if p_counter == s_counter:
            res.append(0)
        
        # Sliding window
        l = 0
        for r in range(len(p), len(s)):
            # Add new character to the window
            s_counter[s[r]] = 1 + s_counter.get(s[r], 0)
            # Remove the left character from the window
            s_counter[s[l]] -= 1
            if s_counter[s[l]] == 0:
                del s_counter[s[l]]  # Remove char if count is zero
            l += 1
            
            # Check if the current window is an anagram
            if p_counter == s_counter:
                res.append(l)
        
        return res

        