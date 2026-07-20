class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = []
        time = []
        for task, freq in count.items():
            heapq.heappush(heap, (-freq, task))
        cycles, t = 0, 0
        while heap or time:
            while time and time[0][0] <= t:
                t1, freq, task = heapq.heappop(time)
                heapq.heappush(heap, (freq, task))
            if heap:
                freq, task = heapq.heappop(heap)
                freq += 1
                if freq < 0:
                    heapq.heappush(time, (t + n + 1, freq, task))
            cycles += 1

            t += 1
        return cycles

