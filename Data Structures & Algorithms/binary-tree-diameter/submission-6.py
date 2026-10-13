# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None: return 0
        res = 0

        def dfs(node):
            nonlocal res

            if node == None or node == 0:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            res = max(res,left+right)

            return max(left,right) + 1


        dfs(root)

        return res

    
    # Idea
    # Go through the tree and compare the left and right heights at each node
    # save the longest path if it is indeed the longest

# IDEA
# calculate height of left and right tree
# at each step grab the left to right and compare with ret