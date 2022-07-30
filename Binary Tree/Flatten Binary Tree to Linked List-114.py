# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return None
        node = root
        while node:
            if node.left:
                rightMost = node.left
                while rightMost.right:
                    rightMost = rightMost.right
                    
                rightMost.right = node.right
                node.right = node.left
                node.left = None
            node = node.right
            