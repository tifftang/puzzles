class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        current = 0
        candidate = 0
        total = 0

        for idx, (g, c) in enumerate(zip(gas, cost)):
            current += g
            current -= c
            total += g
            total -= c

            if current < 0:
                current = 0
                candidate = idx + 1
        return candidate if total >= 0 else -1