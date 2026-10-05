# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return self.search(root, p, q)
    def search(self, node, p, q):
        if node.val > p.val and node.val > q.val:
            return self.search(node.left, p, q)
        elif node.val < p.val and node.val < q.val:
            return self.search(node.right, p, q)
        else:
            return node
        