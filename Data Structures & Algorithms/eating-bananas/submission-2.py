import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m = max(piles)
        n = len(piles)
        l, r = 1, m

        while l < r:
            mid = l + (r - l)//2
            result = sum(math.ceil(a/mid) for a in piles)
            if result > h:
                l = mid + 1
            else:
                r = mid 
        return l
