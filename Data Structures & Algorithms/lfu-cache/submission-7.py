class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.d = defaultdict(OrderedDict)
        self.min_freq = 1

    def update(self, key: int, value:int) -> int:
        val, freq = self.cache[key]
        if value:
            val = value
        del self.d[freq][key]
        if self.min_freq == freq and not len(self.d[freq]):
            self.min_freq = freq + 1
        self.d[freq + 1][key] = val
        self.cache[key] = (val, freq + 1)
        return val

    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        return self.update(key, None)

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.update(key, value)
        else:
            if self.capacity == len(self.cache):
                freq = self.min_freq
                k, v = self.d[freq].popitem(last=False)
                del self.cache[k]
            self.cache[key] = (value, 1)
            self.d[1][key] = value
            self.min_freq = 1



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)