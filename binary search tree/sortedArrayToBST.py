from typing import Optional, List

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums)==0:
            return None
        mid_num = len(nums)//2
        node = TreeNode(nums[mid_num])
        node.left = self.sortedArrayToBST(nums[:mid_num])
        node.right = self.sortedArrayToBST(nums[mid_num+1:])
        return node


if __name__ == "__main__":

    bst = Solution()

    print(bst.sortedArrayToBST(nums=[-10, -3, 0, 5, 9]))
