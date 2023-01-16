from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):

        self.val = val
        self.right = right
        self.left = left


class Solution:

    def getTarget(self, root: Optional[TreeNode], k: int) -> bool:
        output = []
        self.inorder(root, output)

        if len(root) <= 1:
            return False

        i, j = 0, len(output) - 1
        while i < j:
            sum = output[i] + output[j]
            if sum == k:
                return True
            elif sum < k:
                i += 1
            else:
                j -= 1
        return False

    def inorder(self, root, output):

        if root is None:
            return

        else:
            self.inorder(root.left, output)
            output.append(root.val)
            self.inorder(root.right, output)
