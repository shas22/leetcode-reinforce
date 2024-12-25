# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root):

        ans = []
        if not root:
            return ans

        q = [root]
        while q:
            ans.append(max(map(lambda e: e.val, q)))

            currentq = []

            for n in q:
                if n.left:
                    currentq.append(n.left)

                if n.right:
                    currentq.append(n.right)

            q = currentq

        return ans