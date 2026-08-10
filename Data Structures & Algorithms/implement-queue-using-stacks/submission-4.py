class MyQueue:

    def __init__(self):
        self.q = []
        self.r = []

    def push(self, x: int) -> None:
        if not self.q:
            self.q.append(x)
        else:
            while self.q:
                self.r.append(self.q.pop())
            self.r.append(x)
            while self.r:
                self.q.append(self.r.pop())

    def pop(self) -> int:
        return self.q.pop()

    def peek(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()