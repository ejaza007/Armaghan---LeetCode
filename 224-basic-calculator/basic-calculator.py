class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        result = 0
        sign = 1

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == '+':
                result += sign * num
                num = 0
                sign = 1
            elif char == '-':
                result += sign * num
                num = 0
                sign = -1
            elif char == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif char == ')':
                result += sign * num
                num = 0
                result *= stack.pop()
                result += stack.pop()

        result += sign * num
        return result

# Create an instance of the Solution class
sol = Solution()

# Test cases
print(sol.calculate("1 + 1"))        # Output: 2
print(sol.calculate(" 2-1 + 2 "))    # Output: 3
print(sol.calculate("(1+(4+5+2)-3)+(6+8)"))  # Output: 23
