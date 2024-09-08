class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != "]":
                # Push current character to the stack
                stack.append(s[i])
            else:
                # Start popping from stack until we find '['
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                # Remove the '[' from the stack
                stack.pop()

                # Now, we need to extract the number (multiplier)
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                # Repeat the substring k times and push back to stack
                stack.append(int(k) * substr)
        
        # Finally, join everything in the stack and return the result
        return "".join(stack)
