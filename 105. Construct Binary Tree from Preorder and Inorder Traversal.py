def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        m = inorder.index(preorder[0])
        res = TreeNode(preorder[0])
        res.left = self.buildTree(preorder[1:m + 1], inorder[:m])
        res.right = self.buildTree(preorder[m + 1:], inorder[m+1:])
        return res
