# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(bt, greatest):
            if not bt:
                return 0
            good = 1 if bt.val >= greatest else 0
            greatest = max(greatest, bt.val)

            return good + dfs(bt.left, greatest) + dfs(bt.right, greatest)

        return dfs(root, root.val)
        
            
