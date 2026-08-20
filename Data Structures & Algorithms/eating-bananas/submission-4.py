class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        m = max(piles)
        l, r = 1, m

        while l < r:
            mid = l + (r - l)//2
            hours = sum(math.ceil(p/mid) for p in piles)
            #print(hours)
            if hours > h:
                l = mid + 1
            else:
                r = mid
        return l