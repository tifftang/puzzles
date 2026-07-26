class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        def isPali(l, r):
            while l < r:
                if s[l] != s[r]: return False
                l += 1
                r -= 1
            return True

        def bt(i, ans):
            if i == len(s):
                result.append(ans)
                return
            
            for j in range(i + 1, len(s) + 1):
                if isPali(i, j - 1):
                    bt(j, ans + [s[i:j]])
        bt(0, [])
        return result