class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            if stack and a < 0 and stack[-1] > 0:
                broke = False
                while stack and a < 0 and stack[-1] > 0 and abs(a) > stack[-1]:
                    stack.pop()
                    broke = True
                if stack and a < 0 and stack[-1] > 0 and abs(a) == stack[-1]:
                    stack.pop()
                elif stack and a < 0 and stack[-1] > 0 and abs(a) < stack[-1]:
                    continue
                elif not stack or (stack and a < 0 and stack[-1] < 0):
                    stack.append(a)

            else:
                stack.append(a)
        return stack