class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        is_palindrome = [[False] * n for _ in range(n)]

        # Build from shorter substrings to longer substrings.
        for l in range(n - 1, -1, -1):
            for r in range(l, n):
                if s[l] == s[r] and (
                    r - l <= 2 or is_palindrome[l + 1][r - 1]
                ):
                    is_palindrome[l][r] = True

        result = []

        def bt(start, current):
            if start == n:
                result.append(current[:])
                return

            for end in range(start, n):
                if is_palindrome[start][end]:
                    current.append(s[start:end + 1])
                    bt(end + 1, current)
                    current.pop()

        bt(0, [])
        return result