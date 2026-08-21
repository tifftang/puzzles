class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        res = []
        def bt(ans):
            if len(ans) == len(nums):
                res.append(ans[:])
                return
            for num in count:
                if count[num] == 0:
                    continue
                
                ans.append(num)
                count[num] -= 1
                bt(ans)
                count[num] += 1
                ans.pop()
        bt([])
        return res