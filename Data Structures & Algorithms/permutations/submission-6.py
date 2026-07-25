class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def bt(ans, start):
            if start == len(nums):
                result.append(nums[:])
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                bt(ans, start + 1)
                nums[start], nums[i] = nums[i], nums[start]
        
        bt([], 0)
        return result