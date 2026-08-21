class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def bt(start):
            if start == len(nums):
                res.append(nums[:])
                return
            for i in range(start, len(nums)):
                nums[i], nums[start] = nums[start], nums[i]
                bt(start + 1)
                nums[i], nums[start] = nums[start], nums[i]
        bt(0)
        return res