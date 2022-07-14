# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if preorder:
            INDEX = preorder.index(postorder.pop())
            root = TreeNode(preorder[INDEX])
            
            if postorder and postorder[-1] in preorder:
                pivot = preorder.index(postorder[-1])
                root.right = self.constructFromPrePost(preorder[pivot:],postorder)
                root.left = self.constructFromPrePost(preorder[INDEX+1:pivot],postorder)
            
            return root 