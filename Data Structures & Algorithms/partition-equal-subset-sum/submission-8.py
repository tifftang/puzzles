
from functools import cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        half = total // 2
        if total % 2 == 1: return False  

        @cache
        def bt(i, current):
            if current == half: return True
            if current > half: return False
            if i == len(nums): return False

            return bt(i + 1, current) or bt(i + 1, current + nums[i])
        return bt(0, 0)
