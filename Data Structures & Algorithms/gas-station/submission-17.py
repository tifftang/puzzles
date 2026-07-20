class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        current = 0
        candidate = 0
        total = 0
        for i in range(len(gas)):
            g, c = gas[i], cost[i]
            current = current + g - c
            total = total + g - c
            if current < 0:
                candidate = (i + 1) % len(gas)
                current = 0
        return candidate if total >= 0 else -1