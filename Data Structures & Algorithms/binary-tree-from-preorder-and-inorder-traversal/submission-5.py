# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val:idx for idx,val in enumerate(inorder)}
        self.preidx = 0


        def dfs(l,r):
            if l>r:
                return
            
            root_val = preorder[self.preidx]

            root = TreeNode(root_val)

            self.preidx +=1

            mid = indices[root_val]

            root.left = dfs(l,mid-1)
            root.right = dfs(mid+1,r)

            return root




        return dfs(0,len(inorder)-1)
        


        # essentiall move down the preorder list consecutively

        # do a dfs search operation on inorder
            # we should use a a dictionary to map the value to the index for the inorder aray