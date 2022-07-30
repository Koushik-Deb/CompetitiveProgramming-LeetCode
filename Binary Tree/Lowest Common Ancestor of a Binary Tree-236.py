# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def recursion(node):
            if not node: return
            if node==p or node==q:
                return node
            left=recursion(node.left)
            right = recursion(node.right)
            
            if not left: return right
            if not right: return left
            return node
        return recursion(root)