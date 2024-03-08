# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        qu = deque()
        qu.append(root)
        res = []
        while qu:
            right = None
            for i in range(len(qu)):
                curr = qu.popleft()
                if curr.left:
                    qu.append(curr.left)
                if curr.right:
                    qu.append(curr.right)
                right = curr
            if right:
                res.append(right.val)
        return res

