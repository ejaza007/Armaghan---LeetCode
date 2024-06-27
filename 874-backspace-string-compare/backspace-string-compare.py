class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sstack = []
        tstack = []

        for char in s:
            if char == "#":
                if sstack:
                    sstack.pop()
            else:
                sstack.append(char)

        for char in t:
            if char == "#":
                if tstack:
                    tstack.pop()
            else:
                tstack.append(char)

        return sstack == tstack
