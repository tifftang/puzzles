class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bought = None
        profit = 0
        for p in prices:
            if bought == None or bought > p:
                bought = p
            else:
                profit = profit + (p - bought)
                bought = p
        return profit