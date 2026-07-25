class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def bt(used, ans):
            if len(ans) == len(nums):
                result.append(ans)
                return
            for i in range(len(nums)):
                if i not in used:
                    used.add(i)
                    bt(used, ans + [nums[i]])
                    used.remove(i)
        bt(set(), [])
        return result