class Solution:
    def simplifyPath(self, path: str) -> str:
        l = 0
        res = []
        while l < len(path):
            if path[l] == "/":
                if not (res and res[-1] == "/"):
                    res.append(path[l])
                while l < len(path) and path[l] == "/":
                    l += 1
            elif path[l] == ".":
                count = 0
                word = []
                has_ch = False
                while l < len(path) and path[l] != "/":
                    word.append(path[l])
                    if path[l] == ".":
                        count += 1
                    l += 1
                if count != len(word):
                    res.append("".join(word))
                elif count >= 3:
                    res.append("." * count)
                elif count == 2:
                    if len(res) == 1: continue
                    res.pop()
                    res.pop()
            else:
                word = []
                while l < len(path) and path[l] != "/":
                    word.append(path[l])
                    l += 1
                    
                res.append("".join(word))
        if len(res) > 1 and res[-1] == "/":
            res.pop()
        return "".join(res)