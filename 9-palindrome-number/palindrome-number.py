class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        if x < 0:
            return False
        
        # Initialize variables
        original = x
        reversed_num = 0
        
        # Reverse the number
        while x != 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10
        
        # Check if the original number is the same as the reversed number
        return original == reversed_num
