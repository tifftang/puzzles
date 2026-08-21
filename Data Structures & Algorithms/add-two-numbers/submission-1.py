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
        while l1 and l2:
            val = l1.val + l2.val + carry
            if carry:
                carry = 0
            if val > 9:
                carry = 1
            n = ListNode(val % 10)
            temp.next = n
            temp = temp.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            val = l1.val + carry
            if carry:
                carry = 0
            if val > 9:
                carry = 1
            n = ListNode(val % 10)
            temp.next = n
            temp = temp.next
            l1 = l1.next
        while l2:
            val = l2.val + carry
            if carry:
                carry = 0
            if val > 9:
                carry = 1
            n = ListNode(val % 10)
            temp.next = n
            temp = temp.next
            l2 = l2.next     
        if carry: 
            n = ListNode(carry)
            temp.next = n
            temp = temp.next
        return head.next