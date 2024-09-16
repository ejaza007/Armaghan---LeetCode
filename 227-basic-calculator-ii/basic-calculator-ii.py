class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0

        stack = []
        current_num = 0
        operation = '+'
        s += '+'  # Append a '+' to handle the last number

        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char in '+-*/':
                # Process the previous operation with current_num
                if operation == '+':
                    stack.append(current_num)
                elif operation == '-':
                    stack.append(-current_num)
                elif operation == '*':
                    stack[-1] = stack[-1] * current_num
                elif operation == '/':
                    # Integer division truncated towards zero
                    stack[-1] = int(stack[-1] / current_num)

                # Update operation to the current operator
                operation = char
                # Reset current_num for the next number
                current_num = 0

        # Sum up all numbers in the stack for the result
        return sum(stack)

