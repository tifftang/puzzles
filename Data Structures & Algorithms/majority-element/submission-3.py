class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major, freq = nums[0], 0

        for i in range(len(nums)):
            if nums[i] == major:
                freq += 1
            else:
                freq -= 1
            if not freq:
                major = nums[i]
                freq = 1
        return major