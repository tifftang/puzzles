import bisect
class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = []
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d: return ""
        timestamps = self.d[key]
        
        def bs():
            l, r = 0, len(timestamps) - 1
            if len(timestamps) == 0 or timestamps[0][0] > timestamp:
                return 0
            while l <= r:
                mid = l + (r - l)//2
                if timestamps[mid][0] == timestamp:
                    return mid
                elif timestamps[mid][0] > timestamp:
                    r = mid - 1
                else:
                    l = mid + 1
            return l - 1
        idx = bs() 
        idx = idx if idx != len(timestamps) else -1
        ts = timestamps[idx][0]
        if ts > timestamp: return ""
        return self.d[key][idx][1]



