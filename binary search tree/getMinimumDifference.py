from typing import Optional


class TreeNode:

    def __init__(self, val=0, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left


class Solution:

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        output = []
        self.inorder(root, output)
        min_diff = float('inf')
        for i in range(1, len(output)):
            min_diff = min(min_diff, output[1] - output[0])
            print(min_diff)
        return min_diff

    def inorder(self, root, output):
        if root == None:
            return

        else:
            self.inorder(root.left, output)
            output.append(root.val)
            self.inorder(root.right, output)


if __name__ == "__main__":

    tree = TreeNode(val=5)
    tree.left = 4
    tree.right = 6

    sol = Solution()
    sol.getMinimumDifference(5)




