# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        current = root
        stack = []
        
        while True:
            if current:
                stack.append(current)
                result.append(current.val)
                current = current.left
            
            elif stack:
                current = stack.pop().right
        
            else:
                break
        return result
#         result = []
#         def preorder(node):
#             if node:
#                 result.append(node.val)
#                 preorder(node.left)
#                 preorder(node.right)
                
#         preorder(root)
#         return result