class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}

        for idx, n in enumerate(nums):
            if n in d:
                if abs(d[n] - idx) <= k: return True
            d[n] = idx
        return False