from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        arithmeticset = {"+", "-", "/", "*"}

        for s in tokens:
            if s not in arithmeticset:
                stack.append(int(s))  # Convert string to integer and append
            else:
                num1 = stack.pop()  # Operand 1
                num2 = stack.pop()  # Operand 2

                if s == "+":
                    stack.append(num2 + num1)  # Correct addition
                elif s == "-":
                    stack.append(num2 - num1)  # Correct subtraction
                elif s == "/":
                    stack.append(int(num2 / num1))  # Correct integer division
                elif s == "*":
                    stack.append(num2 * num1)  # Correct multiplication

        return stack.pop()  # The result should be the last remaining element

