from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Start with the first string in the array as the initial prefix
        prefix = strs[0]

        for string in strs[1:]:
            # Reduce the prefix length until it matches the start of the current string
            while string[:len(prefix)] != prefix:
                prefix = prefix[:-1]
                # If the prefix is reduced to an empty string, return it
                if not prefix:
                    return ""

        return prefix
