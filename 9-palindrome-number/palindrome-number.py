class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False
        xstring = str(x)

        l,r = 0, len(xstring) - 1

        while l<=r:
            if xstring[l] == xstring[r]:
                l+=1
                r-=1
            else:
                return False
        return True
        