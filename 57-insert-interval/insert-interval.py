from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # If the current interval is after the new interval, just insert the new interval and return the result
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # If the current interval is before the new interval, just add it to the result
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # If the current interval overlaps with the new interval, merge them
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        # Append the new (merged) interval at the end, if not already added
        res.append(newInterval)

        return res



        