from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # Create a counter for the characters in the text
        char_count = Counter(text)
        
        # The word "balloon" has specific character counts
        balloon_count = Counter("balloon")
        
        # Determine the maximum number of "balloon"s we can form
        min_balloons = float('inf')
        
        for char in balloon_count:
            # Calculate how many times we can use this character
            min_balloons = min(min_balloons, char_count[char] // balloon_count[char])
        
        return min_balloons

# Example usage
solution = Solution()
text = "nlaebolko"
print(solution.maxNumberOfBalloons(text))  # Output: 1
