from functools import cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def bt(i, amt):

            if i == len(nums):
                if not amt: 
                    return 1
                return 0
            
            a = bt(i + 1, amt + nums[i])
            b = bt(i + 1, amt - nums[i])
            return a + b
        return bt(0, target)