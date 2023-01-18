from typing import Optional


class TreeNode:

    def __init__(self,val=0, left=None, right=None):
        self.val = val
        self.left= left
        self.right = right

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        ls = []
        self.inorder(root, ls)
        diff = float('inf')

        for i in range(1, len(ls)):
            diff = min(diff, ls[i] - ls[i-1])
        return diff

    def inorder(self, root, ls):
        if root is None:
            return

        self.inorder(root.left, ls)
        ls.append(root.val)
        self.inorder(root.right, ls)