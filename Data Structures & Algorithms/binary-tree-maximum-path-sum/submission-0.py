# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = root.val
        self.calculate(root)
        return self.maxSum

    def calculate( self, node):
        if not node:
            return 0

        leftMax = self.calculate(node.left)
        rightMax = self.calculate(node.right)
        leftMax = max(leftMax, 0)
        rightMax = max(rightMax, 0)

        self.maxSum = max(self.maxSum, node.val + leftMax + rightMax)
        return node.val + max(leftMax, rightMax)
