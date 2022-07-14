# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        current = root
        
        while True:
            if current:
                stack.append(current)
                current = current.left
            elif stack:
                parent = stack.pop()
                result.append(parent.val)
                
                current = parent.right
            else:
                break;
        
        return result
        
        
#         result = []
        
#         def inorder(node):
#             if node:
#                 inorder(node.left)
#                 result.append(node.val)
#                 inorder(node.right)
                
#         inorder(root)
#         return result