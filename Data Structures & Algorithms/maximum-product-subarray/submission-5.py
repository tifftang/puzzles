class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_min, cur_max = nums[0], nums[0]
        result = nums[0]
        for n in nums[1:]:
            candidates = (n, n * cur_min, n * cur_max)
            result = max(cur_max, result)
            cur_max = max(candidates)
            cur_min = min(candidates)
        return max(cur_max, result)