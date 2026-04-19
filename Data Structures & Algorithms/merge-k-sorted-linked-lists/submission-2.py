# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap,(lists[i].val,i,lists[i]))
        
        dummy = ListNode(0)
        cur = dummy
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