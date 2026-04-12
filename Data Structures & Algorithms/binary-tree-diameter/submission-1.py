# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        maxDia = 0

        def dfs(node):
            nonlocal maxDia
            if node==None:
                return 0 

            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)
            diameter = leftHeight + rightHeight
  
            maxDia = max(maxDia,diameter)

            return 1 + max(dfs(node.left),dfs(node.right))
        
        dfs(root)
        return maxDia
        