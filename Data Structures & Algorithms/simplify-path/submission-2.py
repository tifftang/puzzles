class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = [p for p in path.split("/") if p]
        print(parts)
        res = []
        for p in parts:
            if p == "..":
                if res: res.pop()
            elif p == ".":
                continue
            else:
                res.append(p)
        return "/" + ("/").join(res)