# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        def dfs(node, curr_path, curr_sum):
            if not node:
                return
            
            curr_path.append(node.val)

            curr_sum += node.val
            
            if not node.left and not node.right and curr_sum == targetSum:
                result.append(curr_path[:])
            
            dfs(node.left, curr_path, curr_sum)
            dfs(node.right, curr_path, curr_sum)
            
            curr_path.pop()
        
        result = []

        dfs(root, [], 0)
        
        return result