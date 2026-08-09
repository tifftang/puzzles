from functools import cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
            @cache 
            def bt(i, remaining):
                if remaining == 0:
                    return 1
                if i == len(coins): return 0
                times = 0
                if remaining - coins[i] >= 0:
                    times += bt(i, remaining - coins[i])
                times += bt(i + 1, remaining)
                return times
            return bt(0, amount)