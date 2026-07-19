class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        if not self.nums or len(self.nums) != self.k:
            heapq.heappush(self.nums, val)
        elif self.nums[0] < val:
            heapq.heappush(self.nums, val)
            heapq.heappop(self.nums)
        return self.nums[0]
