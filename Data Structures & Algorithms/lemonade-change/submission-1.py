class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        reg = defaultdict(int)

        for b in bills:
            if b == 5:
                reg[b] += 1
            elif b == 10:
                if reg[5] > 0:
                    reg[5] -= 1
                    reg[b] += 1
                else:
                    return False
            elif b == 20:
                amt = 15
                if reg[10] > 0:
                    reg[10] -= 1
                    amt -= 10
                while reg[5] > 0 and amt > 0:
                    reg[5] -= 1
                    amt -= 5
                if amt > 0: return False

        return True
