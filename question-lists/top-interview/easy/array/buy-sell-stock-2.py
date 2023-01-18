import sys
from typing import List

"""
Best Time to Buy and Sell Stock II

https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/564/
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
         Check price every day, sell if previous day was lower.
         Profit(peak - valley) == Sum(profit(sell everyday if price was lower yestreday))
         Example: If a[5] is peak, a[2] is valley
         a[5] - a[2] == a[3] - a[2] + a[4] - a[3] + a[5] - a[4]
         RHS = a[3] - a[3] + a[4] - a[4] + a[5] - a[2] == LHS
         
        """
        total_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                total_profit += prices[i] - prices[i-1]
        return total_profit

if __name__ == "__main__":
    prices = [int(num) for num in sys.argv[1].split(",")]
    print(Solution().maxProfit(prices))
