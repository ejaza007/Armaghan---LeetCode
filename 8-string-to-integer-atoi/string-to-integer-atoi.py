class Solution:
    def myAtoi(self, s: str) -> int:
        # Step 1: Strip leading whitespace
        s = s.lstrip()
        
        if not s:
            return 0

        # Step 2: Handle optional sign
        sign = 1
        index = 0
        if s[0] in ['-', '+']:
            if s[0] == '-':
                sign = -1
            index += 1

        # Step 3: Convert characters to integer
        result = 0
        while index < len(s) and s[index].isdigit():
            result = result * 10 + int(s[index])
            index += 1

        # Step 4: Apply sign
        result *= sign

        # Step 5: Clamp to 32-bit signed integer range
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if result > INT_MAX:
            return INT_MAX
        if result < INT_MIN:
            return INT_MIN
        
        return result
