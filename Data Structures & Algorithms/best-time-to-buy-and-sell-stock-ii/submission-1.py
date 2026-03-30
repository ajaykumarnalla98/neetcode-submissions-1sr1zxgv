class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        profit = 0
        for i in range(1, len(prices)):
            n = prices[i] - prices[i-1]
            if n > 0:
                profit += n
        return profit