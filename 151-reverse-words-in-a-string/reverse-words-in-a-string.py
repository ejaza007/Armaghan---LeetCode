class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.rstrip()
        slist = s.split()

        l,r = 0, len(slist) - 1

        while l<=r:
            slist[l],slist[r] = slist[r], slist[l]
            l+=1
            r-=1

        return ' '.join(slist)
        