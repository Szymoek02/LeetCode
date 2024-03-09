# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(bts, left, right):
            if not bts:
                return True 
            if not (left < bts.val and bts.val < right):
                return False
            return valid(bts.left, left, bts.val) and valid(bts.right, bts.val, right)
        return valid(root, float("-inf"), float("inf"))
