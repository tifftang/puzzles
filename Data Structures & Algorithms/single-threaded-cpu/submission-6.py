class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        time = []
        avail = []
        for idx, (enqueue, process) in enumerate(tasks):
            heapq.heappush(time, (enqueue, process, idx))
        t = 1
        res = []
        while time or avail:
            while time and time[0][0] <= t:
                _, process, idx = heapq.heappop(time)
                heapq.heappush(avail, (process, idx))
            
            if avail:
                process, idx = heapq.heappop(avail)
                t += process
                res.append(idx)
            else:
                t = time[0][0]
        return res