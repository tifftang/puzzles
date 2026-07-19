class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        self.nlarge = []

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if not self.nlarge or self.nlarge[-1] < val:
            self.nlarge = heapq.nlargest(self.k, self.nums)
        return self.nlarge[-1]
