class Solution:
    def buildTree(self, inorder, postorder):
        if not inorder:
            return None

        root = TreeNode(postorder[-1])
        i = inorder.index(postorder[-1])

        root.left = self.buildTree(inorder[:i], postorder[:i])
        root.right = self.buildTree(inorder[i+1:], postorder[i:-1])

        return root