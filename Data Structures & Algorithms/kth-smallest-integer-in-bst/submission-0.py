# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        return self.smallGuy(root, k)

    def smallGuy(self, node, k):
        if not node:
            return
        left = self.smallGuy(node.left, k)

        if left is not None:
            return left
        self.count += 1

        if self.count == k:
            return node.val

        return self.smallGuy(node.right, k)

        
