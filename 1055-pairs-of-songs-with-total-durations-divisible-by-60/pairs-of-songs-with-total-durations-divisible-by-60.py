from typing import List

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainder_count = {}
        count = 0

        for t in time:
            remainder = t % 60
            complement = (60 - remainder) % 60
            
            # Add count of songs with the required complement remainder
            if complement in remainder_count:
                count += remainder_count[complement]

            # Update the hashmap with the current remainder
            remainder_count[remainder] = remainder_count.get(remainder, 0) + 1

        return count
