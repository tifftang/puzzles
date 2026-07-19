class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        self.nlarge = []
    def add(self, val: int) -> int:
        if not self.nlarge or self.nlarge[-1] < val:
            heapq.heappush(self.nums, val)
            self.nlarge = heapq.nlargest(self.k, self.nums)
            self.nums = self.nlarge

        return self.nlarge[-1]
