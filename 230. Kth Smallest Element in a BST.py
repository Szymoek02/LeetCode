# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Iteratively
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return
        stack = []
        
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
        return 0

# Recursively
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.result = 0
        self.inorder(root, k)
        return self.result

    def inorder(self, root, count):
        if not root:
            return
        self.inorder(root.left, count)

        self.count += 1
        if count == self.count:
            self.result = root.val

        self.inorder(root.right, count)
