# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        maxVal = root.val
        return self.counter(root, maxVal)

    def counter(self, node, maxVal):
        if node.val >= maxVal:
            self.count += 1
        maxVal = max(maxVal, node.val)
        if node.left:
            self.counter(node.left, maxVal)
        if node.right:
            self.counter(node.right, maxVal)
        return self.count