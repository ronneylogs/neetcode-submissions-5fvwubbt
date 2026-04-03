"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # maps old to new
        # 2 functions
            # make sure we dont make nodes that were already created
            # helps us locate new nodes that are already created
        gMap = {}

        def dfs(node):
            # making sure we aren't creating double and just returning what we already made
            if node in gMap:
                return gMap[node]

            # copy the node
            copy = Node(node.val)

            # add to hashmap
            gMap[node] = copy

            # add each neighbor
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))

            # return itself
            return copy
    
        return dfs(node) if node else None




# RUN DFS on the graph to create a clone

# use a hashmap to map old to new 
# create all nodes first then start connecting neighbours backwards
        