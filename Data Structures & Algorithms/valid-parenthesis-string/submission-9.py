class Solution:
    def checkValidString(self, s: str) -> bool:
        stars = deque()
        open = deque()
        for idx,ch in enumerate(s):
            if ch == ')':
                if open:
                    open.pop()
                elif stars:
                    stars.popleft()
                else:
                    return False
            elif ch == "(":
                open.append(idx)
            else:
                stars.append(idx)
        #print(open, stars)
        while open and stars:
            val = open.popleft()
            close = stars.popleft()
            while stars and val > close:
                close = stars.popleft()
            if val > close:
                return False
        return True if not open else False