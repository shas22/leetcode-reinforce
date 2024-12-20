# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])

        level = 1

        while q:
            level_count = len(q)
            curr = []

            for _ in range(level_count):
                node = q.popleft()

                if level % 2 == 0:
                    curr.append(node)

                for child in [node.left, node.right]:
                    if child:
                        q.append(child)

            left, right = 0, len(curr) - 1

            while left < right:
                curr[left].val, curr[right].val = curr[right].val, curr[left].val

                left += 1
                
                right -= 1
                
            level += 1

        return root