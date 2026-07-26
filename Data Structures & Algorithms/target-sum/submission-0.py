class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.result = 0

        def bt(i, amt):
            if i == len(nums):
                if not amt: 
                    self.result += 1
                return
            
            bt(i + 1, amt + nums[i])
            bt(i + 1, amt - nums[i])
        bt(0, target)
        return self.result