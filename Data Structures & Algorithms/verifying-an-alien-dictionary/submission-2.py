class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {}
        for i in range(len(order)):
            d[order[i]] = i
        print(d)
        for i in range(1, len(words)):
            w1 = words[i - 1]
            w2 = words[i]
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if d[c1] > d[c2]:
                        return False
                    break
            else:
                if len(w1) > len(w2): return False
        return True