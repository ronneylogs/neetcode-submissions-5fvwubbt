# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        og = root.val
        self.res = 0

        def dfs(node,prev):
            if node == None:
                return 
            
            if node.val >= prev:
                self.res += 1

            prev = max(prev,node.val)
            dfs(node.left,prev)
            dfs(node.right,prev)

            return 
        
        dfs(root,root.val)

        return self.res

        # idea
            # 