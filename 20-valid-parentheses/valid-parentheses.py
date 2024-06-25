class Solution:
    def isValid(self, s: str) -> bool:
        paraset = {")": "(" , "]":"[", "}" : "{"}
        stack = []

        for c in s:
            if c in paraset:
                if stack and stack[-1] == paraset[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

        