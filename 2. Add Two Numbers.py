# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tail = ListNode()
        dummy = tail
        carry = 0
        while l1 or l2 or carry:
            x1 = l1.val if l1 else 0
            x2 = l2.val if l2 else 0
            #18
            s = x1 + x2 + carry
            carry = s // 10
            dummy.next = ListNode(s % 10)
            dummy = dummy.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return tail.next

