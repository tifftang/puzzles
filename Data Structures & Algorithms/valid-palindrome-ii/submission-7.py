class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        done = False

        def check(l, r):
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1             
                else: return False
            return True   

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return check(l + 1, r) or check(l, r-1)
        return True