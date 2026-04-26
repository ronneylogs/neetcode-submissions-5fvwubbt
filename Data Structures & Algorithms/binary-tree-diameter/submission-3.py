# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0 

        def dfs(node):
            nonlocal diameter
            if node == None:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            diameter = max(diameter,left+right)

            return 1+max(left,right)

        dfs(root)
    
        return diameter



        # we want to pass info to the parent, so post order traversal
        # base case if null

        # pass the length of longest child to parent

        # use a diameter vartiable to keep track of the longest instance
        