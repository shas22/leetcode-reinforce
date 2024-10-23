# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def replaceValueInTree(self, root):

        if not root:
            return None
            
        q = [(root, root.val)]
        
        while q:

            new_q = []

            level_sum = 0
            for node, _ in q:
                level_sum += node.val
            
            for node, parent in q:

                node.val = level_sum - parent
                

                children = [node.left, node.right]

                children_sum = sum(child.val for child in children if child)
                

                new_q.extend((child, children_sum) for child in children if child)
                
            q = new_q
            
        return root