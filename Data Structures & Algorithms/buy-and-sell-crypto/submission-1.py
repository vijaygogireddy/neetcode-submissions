class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        min_price = 101

        for price in prices:
            min_price = min(price, min_price)

            if price > min_price:
                max_profit = max(max_profit, price - min_price)

        return max_profit


        
        # O(n^2)
        res = 0
        n = len(prices)
        for i in range(n):
            for j in range(i+1, n):
                res = max(res, prices[j] - prices[i])

        return res