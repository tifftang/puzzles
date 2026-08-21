class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def bt(start):
            if start == len(nums):
                res.append(nums[:])
                return
            seen = set()
            for i in range(start, len(nums)):
                if nums[i] not in seen:
                    nums[i], nums[start] = nums[start], nums[i]
                    bt(start + 1)
                    nums[i], nums[start] = nums[start], nums[i]
                    seen.add(nums[i])
        bt(0)
        return res