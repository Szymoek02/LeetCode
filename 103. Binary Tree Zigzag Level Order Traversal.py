# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        qu = deque()
        qu.append(root)
        
        flag = False
        while qu:
            level = []
            for _ in range(len(qu)):
                node = qu.popleft()
                if node:
                    level.append(node.val)
                if node.right:
                    qu.append(node.right)
                if node.left:
                    qu.append(node.left)
            flag = not flag
            if flag: level.reverse()
            res.append(level)
        return res
