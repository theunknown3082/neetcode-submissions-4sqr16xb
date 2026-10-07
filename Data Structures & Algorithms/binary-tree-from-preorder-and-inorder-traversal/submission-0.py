# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preIdx, self.inIdx = 0, 0
        self.preorder = preorder
        self.inorder = inorder
        return self.dfs(float("inf"))

    def dfs(self, node):
        if self.preIdx >= len(self.preorder):
            return None
        if self.inorder[self.inIdx] == node:
            self.inIdx += 1
            return None
        root = TreeNode(self.preorder[self.preIdx])
        self.preIdx += 1
        root.left = self.dfs(root.val)
        root.right = self.dfs(node)
        return root