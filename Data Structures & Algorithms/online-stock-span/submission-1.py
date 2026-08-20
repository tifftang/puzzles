class StockSpanner:

    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        val = (price, 1)
        while self.prices and price >= self.prices[-1][0]:
            last_price, last_span = self.prices.pop()
            val = val[0], last_span + val[1]
        self.prices.append(val)

        return val[1]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)