# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def dfs(node):
            if node == None:
                return None
            
            dfs(node.left)
            res.append(node)
            dfs(node.right)
        
            return

        dfs(root)
        return res[k-1].val

        

        # Idea
        # do an inorder traversal
        # add items it list
        # return the ith item in the list