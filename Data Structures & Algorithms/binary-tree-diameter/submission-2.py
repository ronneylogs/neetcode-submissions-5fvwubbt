# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return []

        res = 0
        
        def dfs(n):
            nonlocal res
            if n == None:
                return 0

            left = dfs(n.left)
            right = dfs(n.right)

            added = left + right

            res = max(res,added)
            return 1+ max(left,right)

        
        dfs(root)

        return res


        # for the iterative step, I am constantly grabbing the largest child


        