# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        current = root
        
        while True:
            if current:
                stack.append(current)
                current = current.left
            
            elif stack:
                top = stack[-1]
                if top.right is None:
                    result.append(top.val)
                    stack.pop()
                if stack and stack[-1].right and result and  stack[-1].right.val == result[-1]:
                    result.append(stack.pop().val)
                elif stack:
                    current = stack[-1].right
            else:
                break
        return result
        
#         result = []
        
#         def postorder(node):
#             if node:
#                 postorder(node.left)
#                 postorder(node.right)
#                 result.append(node.val)
                
#         postorder(root)
#         return result