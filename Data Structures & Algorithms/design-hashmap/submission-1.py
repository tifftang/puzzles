class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

class MyHashMap:

    def __init__(self):
        self.map = [LinkedList() for _ in range(10000)]

    def put(self, key: int, value: int) -> None:
        k = key % 10000
        lst = self.map[k].head.next
        while lst:
            if lst.key == key:
                lst.val = value
                return
            lst = lst.next
        n = Node(key, value)
        tail = self.map[k].tail
        tmp = tail.prev
        tmp.next = n
        tail.prev = n
        n.next = tail
        n.prev = tmp

    def get(self, key: int) -> int:
        k = key % 10000
        lst = self.map[k].head.next
        while lst:
            if lst.key == key:
                return lst.val
            lst = lst.next
        return -1

    def remove(self, key: int) -> None:
        k = key % 10000
        lst = self.map[k].head.next
        while lst:
            if lst.key == key:
                prev = lst.prev
                next = lst.next
                prev.next = next
                next.prev = prev
                return
            lst = lst.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)