class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def bt(ans):
            if len(ans) == len(nums):
                if len(set(ans)) == len(nums):
                    result.append(ans)
                return
            for i in range(len(nums)):
                bt(ans + [nums[i]])
        bt([])
        return result