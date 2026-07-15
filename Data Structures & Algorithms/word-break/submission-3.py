class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def bt(i):
            if i == len(s): return True
            if i in memo: return memo[i]
            for word in wordDict:
                if s[i:].startswith(word):
                    if bt(i + len(word)): return True
            memo[i] = False
            return False
        return bt(0)