# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        ret = 0

        def dfs(n):
            nonlocal ret

            if n is None:
                return 0
            
            left = dfs(n.left)
            right = dfs(n.right)

            ret = max(ret,right+left)

            return 1 + max(left,right)


        dfs(root)
        return ret
        


# IDEA
# calculate height of left and right tree
# at each step compare the length of left and right and take bigger answer
# 