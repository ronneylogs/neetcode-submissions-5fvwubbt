# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        # Add each list to to the heap ranked by the first 
        # e.g store [1,2,4] -> (1,0,[1,2,4])
                  # [1,3,5] -> (1,1,[1,3,5])
                  # [3,6] -> (3,2,[3,6])
            # heapq = [(1,0,node[1]),(1,1,node[1]),(3,2,node[3])]
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap,(lists[i].val,i,lists[i]))
        

        dummy = ListNode(0)
        cur = dummy

        # While heap still has item, add item to LL, after adding that specific item, check if it has next item, if yes then add to heap
        while heap:
            val,index,node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next

            if node.next:
                node = node.next
                heapq.heappush(heap,(node.val,index,node))

        return dummy.next
        
            


        


# Idea
# Use a heap and add the first item of each list to the heap, (node.val,i,node)
# While the heap isn't empty, lets keep pushing items onto the heap