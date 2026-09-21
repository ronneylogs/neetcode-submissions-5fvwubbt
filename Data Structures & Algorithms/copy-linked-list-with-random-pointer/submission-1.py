"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        dummy = Node(0,None)

        cur = dummy

        orig = head
        prevOrig = Node(0,head)

        while orig:
            n = Node(orig.val,None)
            cur.val = prevOrig.val

            cur.next = n
            prevOrig  = prevOrig.next
            orig = orig.next
            cur = cur.next
        

        mp  = {}

        orig = head
        cped = dummy.next
        while orig:
            mp[orig] = cped
            orig = orig.next
            cped = cped.next
    
        orig = head
        cped = dummy.next

        while orig:
            if orig.random:
                cped.random = mp[orig.random]
            else:
                cped.random = None
            orig = orig.next
            cped = cped.next
            
        
        return dummy.next
        

        # idea
        # 1. Create the copies and fill in val and next
            # quirk is that we need to always have a node ahead so the next can point to it
        # 2. Build a dictionary where the old node points to the new node
        # 3. Last run is to go through the nodes and add the random pointer
        

