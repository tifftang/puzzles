class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = []
        for _ in range(2):
            for n in nums:
                result.append(n)
        return result