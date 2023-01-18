from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ls = []
        def inorder(root, ls):

            if root is None:
                return
            inorder(root.left, ls)
            ls.append(root.val)
            inorder(root.right, ls)

        inorder(root, ls)

        sum_list = []
        
        for i in range(len(ls)):
            if low <= ls[i] <= high:
                sum_list.append(ls[i])

        return sum(sum_list)