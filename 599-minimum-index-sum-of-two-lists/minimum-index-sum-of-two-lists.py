from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        minIndex = float('inf')
        listMap = {}
        res = []

        for i in range(len(list1)):
            listMap[list1[i]] = i
        
        for i in range(len(list2)):
            if list2[i] in listMap:
                indexSum = listMap[list2[i]] + i
                if indexSum < minIndex:
                    res = [list2[i]]
                    minIndex = indexSum
                elif indexSum == minIndex:
                    res.append(list2[i])
        return res
