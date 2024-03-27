# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        res = []
        def dfs(tree):
            if not tree:
                res.append('N')
                return
            res.append(str(tree.val))
            dfs(tree.left)
            dfs(tree.right)
        dfs(root)
        return ','.join(res)

    def deserialize(self, data):
        self.i = 0
        data = data.split(',')
        def dfs():
            if data[self.i] == 'N':
                self.i += 1
                return None
            node = TreeNode(int(data[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
            
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
