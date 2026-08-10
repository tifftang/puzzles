class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = []
        def bt(i, total):
            if i == len(nums):
                res.append(total)
                return
            
            bt(i + 1, total)
            bt(i + 1, total ^ nums[i])
        bt(0, 0)
        return sum(res)
