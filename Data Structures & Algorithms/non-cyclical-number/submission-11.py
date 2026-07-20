class Solution:
    def isHappy(self, n: int) -> bool:
        
        def sumIt(n):
            val = 0
            while n > 0:
                digit = n % 10
                n = n // 10
                val += digit ** 2
            return val
        
        seen = set()
        while True:
            n = sumIt(n)
            if n == 1: return True
            if n in seen: return False
            seen.add(n)

