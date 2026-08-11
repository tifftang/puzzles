class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber:
            columnNumber -= 1
            n = columnNumber % 26
            columnNumber = columnNumber// 26
            res.append(chr(n + ord('a')).upper())
            #print(n, columnNumber)
        #print(res)
        return "".join(reversed(res))