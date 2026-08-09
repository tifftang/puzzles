class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        m = min(len(s) for s in strs)
        result = []
        for i in range(m):
            ltr = strs[0][i]
            for s in strs:
                if s[i] != ltr: 
                    return "".join(result)
            result.append(ltr)
        return "".join(result)