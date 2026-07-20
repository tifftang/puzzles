class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        def bt(i, ans):
            if i == len(nums): 
                result.append(ans)
                return
            n = i
            while n < len(nums) and nums[n] == nums[i]:
                n += 1
            bt(i + 1, ans + [nums[i]])
            bt(n, ans)
        bt(0, [])
        return result