class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def bt(j, last):
            if j in memo: return memo[j]
            max_l = 0
            for i in range(j, len(nums)):
                n = nums[i]
                if n > last:
                    max_l = max(bt(i + 1, n), max_l)
            memo[j] = 1 + max_l
            return memo[j]
        bt(0, -float('inf'))
        return memo[0] - 1