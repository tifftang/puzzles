class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        max_reach = nums[0]
        current_reach = max_reach
        total = 1
        for i in range(1, len(nums) - 1):
            max_reach = max(max_reach, nums[i] + i)
            if current_reach <= i:
                total += 1
                current_reach = max_reach
        return total