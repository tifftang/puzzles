class LinkedList():
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head

class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyHashSet:

    def __init__(self):
        self.hash = [LinkedList() for _ in range(10000)]

    def add(self, key: int) -> None:
        k = key % 10000
        lst = self.hash[k]
        head = lst.head.next
        node = Node(key)

        while head:
            if head.val == key: return
            head = head.next
        
        tmp = lst.tail.prev
        lst.tail.prev = node
        tmp.next = node
        node.next = lst.tail
        node.prev = tmp


    def remove(self, key: int) -> None:
        k = key % 10000
        lst = self.hash[k]
        head = lst.head.next

        while head:
            if head.val == key:
                nxt = head.next
                prv = head.prev
                prv.next = nxt
                nxt.prev = prv
                return
            head = head.next

    def contains(self, key: int) -> bool:
        k = key % 10000
        lst = self.hash[k]
        head = lst.head.next
        while head:
            if head.val == key: return True
            head = head.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)