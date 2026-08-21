# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode(0)
        temp = head
        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            val = l1_val + l2_val + carry
            carry = 1 if val > 9 else 0
            n = ListNode(val % 10)
            temp.next = n
            temp = temp.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return head.next