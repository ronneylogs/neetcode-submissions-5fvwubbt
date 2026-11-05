# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None: return 0
        self.big = 0

        def dfs(node):

            if node == None or node == 0:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)


            self.big = max(self.big,left+right)

            return max(left,right) + 1



        dfs(root)


        return self.big




        # diametre means we want to know the left right
        # can be the longest path between any two nodes


        # problem boils down to selecting the longest path return by the children at each step
        