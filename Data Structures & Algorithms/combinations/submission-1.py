class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def bt(i, ans):
            if len(ans) == k:
                res.append(ans[:])
                return
            if i > n: return
            
            ans.append(i)
            bt(i + 1, ans)
            ans.pop()
            bt(i + 1, ans)
        bt(1, [])
        return res