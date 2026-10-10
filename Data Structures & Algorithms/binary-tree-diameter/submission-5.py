# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        ret = 0

        def dfs(root):
            nonlocal ret
            if root == None:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            
            ret = max(ret,left+right)

            return max(left,right) + 1


        dfs(root)

        return ret

# IDEA
# calculate height of left and right tree
# at each step grab the left to right and compare with ret