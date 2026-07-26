class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        memo = {}
        def isPali(l, r):
            if (l, r) in memo: return memo[(l, r)]
            o_l, o_r = l, r
            while l < r:
                if s[l] != s[r]: 
                    memo[(l, r)] = False
                    return False
                l += 1
                r -= 1
            memo[(o_l, o_r)] = True
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