class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        d = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        def bt(i, ans):
            if i == len(digits):
                if ans:
                    result.append("".join(ans))
                return
            
            word = d[int(digits[i])]
            for w in word:
                bt(i + 1, ans + [w])
        bt(0, [])
        return result