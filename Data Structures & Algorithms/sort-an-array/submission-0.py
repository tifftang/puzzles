class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        minV, maxV = min(nums), max(nums)
        l = 0
        for i in range(minV, maxV + 1):
            if i in count:
                while count[i] > 0:
                    nums[l] = i
                    count[i] -= 1
                    l += 1
        return nums
            