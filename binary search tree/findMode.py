from typing import Optional, List


class TreeNode:

    def __init__(self, val=0, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left

    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return []
        ls = []

        if root.left == root:
            ls.append(root.left)
            
