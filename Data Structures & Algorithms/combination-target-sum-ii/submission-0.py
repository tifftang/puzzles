class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def bt(i, arr, amt_left):
            if amt_left == 0:
                result.append(arr)
                return
            if i == len(candidates):
                return
            
            if candidates[i] > amt_left: return
            bt(i + 1, arr + [candidates[i]], amt_left - candidates[i])
            j = i + 1
            while j < len(candidates) and candidates[i] == candidates[j]:
                j += 1
            if j < len(candidates):
                bt(j, arr, amt_left)
        bt(0, [], target)
        return result