# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        self.balance(root)
        return self.balanced
        
    def balance(self, node):
        if not node:
            return 0
        rightDepth = self.balance(node.right)
        leftDepth = self.balance(node.left)
        if abs(leftDepth - rightDepth) > 1:
            self.balanced = False
            
        return 1 + max(leftDepth, rightDepth)