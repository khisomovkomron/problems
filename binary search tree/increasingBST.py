from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def increasingBST(self, root: Optional[TreeNode]) -> TreeNode:

        output = []
        self.inorder(root, output)

        tree = TreeNode(val=output[0])
        tmp = tree

        for i in output[1:]:
            tmp.right = TreeNode(val=i)
            tmp = tmp.right
        return tree

    def inorder(self, root, output):
        if root is None:
            return

        self.inorder(root.left, output)
        output.append(root.val)
        self.inorder(root.right, output)