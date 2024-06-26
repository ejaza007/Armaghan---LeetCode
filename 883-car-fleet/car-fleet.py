from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        pair = []
        
        # Create pairs of (position, speed)
        for i in range(n):
            pair.append((position[i], speed[i]))
        
        # Sort the pairs by position in descending order
        pair.sort(reverse=True)
        
        fleets = 0
        last_time = 0
        
        # Calculate time to reach the target and manage fleets
        for p, s in pair:
            time = (target - p) / s
            if time > last_time:
                fleets += 1
                last_time = time
        
        return fleets
