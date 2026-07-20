class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def bt(i, ans):
            if i == len(nums): 
                result.append(deepcopy(ans))
                return
            
            bt(i + 1, ans)
            bt(i + 1, ans + [nums[i]])
        bt(0, [])
        return result
