class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump = nums[0]

        for idx, n in enumerate(nums):
            if jump < idx: return False
            jump = max(jump, idx + n)
        return True
