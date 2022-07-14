# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            INDEX = inorder.index(postorder.pop())
            root = TreeNode(inorder[INDEX])
            
            root.right = self.buildTree(inorder[INDEX+1:],postorder)
            root.left = self.buildTree(inorder[:INDEX],postorder)
            
            return root
        