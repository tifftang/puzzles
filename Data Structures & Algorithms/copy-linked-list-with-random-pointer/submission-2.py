"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new_head = Node("0")
        dummy = new_head
        seen = {}
        while head:
            #print(head.val)
            next_node = seen[head] if head in seen else Node(str(head.val))
            rand_node = None

            seen[head] = next_node
            if head.random:
                if head.random in seen:
                    rand_node = seen[head.random]
                else:
                    rand_node =  Node(str(head.random.val))
            new_head.next = next_node
            next_node.random = rand_node
            if rand_node:
                seen[head.random] = rand_node
            new_head = new_head.next
            head = head.next
        return dummy.next


