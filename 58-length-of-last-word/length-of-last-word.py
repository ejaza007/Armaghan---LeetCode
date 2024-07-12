class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Trim any trailing spaces
        s = s.rstrip()
        # Split the string into words
        words = s.split(' ')
        # Return the length of the last word
        return len(words[-1])

# Example usage:
sol = Solution()
print(sol.lengthOfLastWord("Hello World"))  # Output: 5
print(sol.lengthOfLastWord("   fly me   to   the moon  "))  # Output: 4
print(sol.lengthOfLastWord("luffy is still joyboy"))  # Output: 6


