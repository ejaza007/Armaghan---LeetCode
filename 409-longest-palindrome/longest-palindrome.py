from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        length = 0
        odd_found = False

        for count in counter.values():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1
                odd_found = True
        
        # If there is any odd count, we can place one character in the center
        if odd_found:
            length += 1
        
        return length
