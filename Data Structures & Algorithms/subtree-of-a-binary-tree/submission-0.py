# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root:
            return False
        return (
            self.check(root, subRoot)
            or self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot))

    def check(self, p, q):
        if not p and not q:
            return True
        elif (p == None and q != None) or (p != None and q == None):
            return False
        elif p.val != q.val:
            return False

        right = self.check(p.right, q.right)
        left = self.check(p.left, q.left)
        return right and left 