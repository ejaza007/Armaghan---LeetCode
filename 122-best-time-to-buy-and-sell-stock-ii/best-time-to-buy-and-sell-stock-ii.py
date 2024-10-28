from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0  # Initialize the maximum profit
        
        for i in range(1, len(prices)):
            # If today's price is higher than yesterday's price, we can profit
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        
        return max_profit
