class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = -prices[0]
        cash = 0

        for p in prices[1:]:
            new_hold = max(hold, cash - p)
            new_cash = max(cash, hold + p)
            hold, cash = new_hold, new_cash
        return cash