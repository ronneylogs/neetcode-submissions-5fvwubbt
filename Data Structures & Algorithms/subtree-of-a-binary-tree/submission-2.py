# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # check if subroot exists
        if subRoot==None:
            return True
        # check if root exists
        if root == None:
            return False
        # check if they are same from the root
        if self.sameTree(root,subRoot):
            return True
        # do the same for both the left and right child of the root
        children = self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

        return children
    def sameTree(self,root,subRoot):
        if root == None and subRoot == None:
            return True
        


        

        if subRoot and root and subRoot.val == root.val:
            return (self.sameTree(root.left,subRoot.left)) and (self.sameTree(root.right,subRoot.right))

            

        return False
            

# Passing down:
    # two trees
# Passing up:
    # False if they are not the same

# Assume all is true, if at the end we get passed a False anywhere along the way then that means that something is wrong