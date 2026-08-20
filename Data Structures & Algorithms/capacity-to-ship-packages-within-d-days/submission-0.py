class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        m = max(weights)
        n = sum(weights)
        l, r = m, n

        while l < r:
            mid = l + (r - l)//2
            d, carry = 1, 0
            for w in weights:
                if (carry + w) <= mid:
                    carry += w
                else:
                    carry = w
                    d += 1
            if d > days:
                l = mid + 1
            else:
                r = mid
        return l


