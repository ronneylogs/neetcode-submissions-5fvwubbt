# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        def dfs(node):
            if node is None:
                return None
            
            node.left,node.right = dfs(node.right),dfs(node.left)

            return node


        return dfs(root)


        