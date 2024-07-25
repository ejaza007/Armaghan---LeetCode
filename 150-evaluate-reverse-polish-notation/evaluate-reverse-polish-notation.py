from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        arithmeticset = {"+", "-", "/", "*"}

        for s in tokens:
            if s not in arithmeticset:
                stack.append(int(s))  
            else:
                num1 = stack.pop()  
                num2 = stack.pop()  

                if s == "+":
                    stack.append(num2 + num1)  
                elif s == "-":
                    stack.append(num2 - num1)  
                elif s == "/":
                    stack.append(int(num2 / num1)) 
                elif s == "*":
                    stack.append(num2 * num1) 

        return stack.pop() 

