# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
       return self.Depth(root) 
        
    def Depth(self, node):
        if not node:
            return 0
        RightDepth = self.Depth(node.right)
        LeftDepth = self.Depth(node.left)

        return 1 + max(RightDepth, LeftDepth)