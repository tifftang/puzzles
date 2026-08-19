class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        value = 0
        min_length = float('inf')
        nums = nums + [0]
        for r in range(len(nums)):
            value += nums[r]
            while l <= r and value >= target:
                min_length = min(min_length, r - l + 1)
                value -= nums[l]
                l += 1
        return min_length if min_length < float('inf') else 0


