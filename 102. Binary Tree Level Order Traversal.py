# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        qu = deque()
        qu.append(root)
        res = []

        while qu:
            level = []
            for i in range(len(qu)):
                node = qu.popleft()
                if node:
                    level.append(node.val)
                if node.left:
                    qu.append(node.left)
                if node.right:
                    qu.append(node.right)

            if level:
                res.append(level)

        return res
