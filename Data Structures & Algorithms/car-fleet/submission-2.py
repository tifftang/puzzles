class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        arr1, arr2 = map(list, zip(*pairs))
        pos = []
        for i in range(len(position)):
            p, s = arr1[i], arr2[i]
            t = ((target - p) / s)
            if pos and pos[-1] > t:
                pos.append(pos[-1])
            else:
                pos.append(t)
        #print(pos)
        #print(arr1, arr2)
        return len(set(pos))
