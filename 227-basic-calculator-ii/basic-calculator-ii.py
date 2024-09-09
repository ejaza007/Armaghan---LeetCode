class Solution:
    def calculate(self, s: str) -> int:
        # Remove all spaces from the string
        s = s.replace(" ", "")
        stack = []
        current_number = 0
        last_operator = '+'
        
        for i, c in enumerate(s):
            if c.isdigit():
                current_number = current_number * 10 + int(c)
                
            if c in "+-*/" or i == len(s) - 1:
                if last_operator == '+':
                    stack.append(current_number)
                elif last_operator == '-':
                    stack.append(-current_number)
                elif last_operator == '*':
                    stack.append(stack.pop() * current_number)
                elif last_operator == '/':
                    # Handle integer division and truncate toward zero
                    stack.append(int(stack.pop() / current_number))
                
                # Reset current number and update the last operator
                current_number = 0
                last_operator = c
        
        # The final result is the sum of the stack
        return sum(stack)
