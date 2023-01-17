import sys
from typing import List

"""
Best Time to Buy and Sell Stock II

https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/564/
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Buy low, sell high
        """
        dir = None
        total_profit = 0
        min_price = float("inf")
        max_profit = 0
        prices.append(-1)
        for i in range(len(prices) - 1):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)
            if prices[i + 1] < prices[i]:
                if not dir:
                    dir = "decreasing"
                if dir == "increasing":
                    # Dip found
                    total_profit += max_profit
                    max_profit = 0
                    min_price = float("inf")
                    dir = "decreasing"
            if prices[i + 1] > prices[i]:
                if not dir:
                    dir = "increasing"
                if dir == "decreasing":
                    dir = "increasing"
        return total_profit

if __name__ == "__main__":
    prices = [int(num) for num in sys.argv[1].split(",")]
    print(Solution().maxProfit(prices))
