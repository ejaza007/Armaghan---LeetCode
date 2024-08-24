class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            newArr = [0] * 26


            for c in s:
                newArr[ord(c) - ord('a')]+=1
            res[tuple(newArr)].append(s)
        return list(res.values())


            
            
            
            

        