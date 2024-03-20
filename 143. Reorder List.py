# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle
        # put second half on the stack
        # node -> stack -> node -> stack
        node = head
        stack = []
        while node:
            stack.append(node)
            node = node.next
        p1 = head
        for _ in range(len(stack) // 2):
            n = stack.pop()
            temp = p1.next
            p1.next = n
            n.next = temp
            p1 = temp
        p1.next = None    
