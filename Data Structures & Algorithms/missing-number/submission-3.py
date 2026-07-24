class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = sum([x for x in range(len(nums) + 1)])
        actualTotal = sum(nums)
        return total - actualTotal