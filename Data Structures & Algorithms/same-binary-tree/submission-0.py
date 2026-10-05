# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.check(p, q)

    def check(self, pNode, qNode):
        if pNode == None and qNode == None:
            return True
        elif (pNode == None and qNode != None) or (pNode != None and qNode == None):
            return False
        elif pNode.val != qNode.val:
            return False
        
        leftCheck = self.check(pNode.left, qNode.left)
        rightCheck = self.check(pNode.right, qNode.right)
        return leftCheck and rightCheck
        