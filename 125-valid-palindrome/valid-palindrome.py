class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Filter out non-alphanumeric characters and convert to lowercase
        filtered_s = ''.join(char.lower() for char in s if char.isalnum())
        
        l, r = 0, len(filtered_s) - 1
        
        while l <=r:
            if filtered_s[l] == filtered_s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
