# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # Store each value's index in inorder for O(1) lookup
        indices = {val:idx for idx,val in enumerate(inorder)}

        self.pre_idx = 0

        # l and r represent the boundaries of the current subtree in inorder
        def dfs(l,r):

                # no nodes left in this subtree, when l>r
                if l>r:
                    return None

                # The next element is always the root of the current subtree
                root_val = preorder[self.pre_idx]
                self.pre_idx += 1

                # Create the root node
                root = TreeNode(root_val)

                # Find the root's position to split left and right subtrees
                mid = indices[root_val]

                # Everything before mid belongs to the left subtree
                root.left = dfs(l,mid-1)

                # Everything after mid belogns to the right subtree
                root.right = dfs(mid+1,r)

                # Return the constructed subtree
                return root


        # Start with the entire inorder array
        return dfs(0,len(inorder) - 1)


    # preorder is the root
    # then find the inorder and look left and right
    # Use dfs to go over left and right subtree
    # At each step build the node, most of the work is managing the two lists
        