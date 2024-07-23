class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if s == "":
            return True
        if len(s) > len(t):
            return False


        sPointer = 0
        tPointer = 0

        while tPointer < len(t):
            if t[tPointer] == s[sPointer]:
                sPointer +=1
                if sPointer == len(s):
                    return True
            tPointer+=1
        return False        