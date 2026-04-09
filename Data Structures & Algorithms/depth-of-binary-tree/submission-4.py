# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root == None:
            return 0

        def dfs(node):
            if node == None:
                return 0
            
            long = max(dfs(node.left),dfs(node.right))

            return long + 1

        
        length1 = dfs(root.left)
     
        length2 = dfs(root.right)


        return max(length1,length2)+1
        