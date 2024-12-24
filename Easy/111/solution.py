# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        
        if root.left and root.right:
            return min(left_depth, right_depth) + 1
    
        elif root.left:
            return left_depth + 1

        elif root.right:
            return right_depth + 1
            
        else:
            return 1