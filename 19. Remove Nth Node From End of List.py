# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(999)
        dummy.next = head
        d = head
        for _ in range(n):
            d = d.next
        
        curr = head
        prev = dummy
        while d:
            prev = curr
            curr = curr.next
            d = d.next

        prev.next = curr.next
        return dummy.next
