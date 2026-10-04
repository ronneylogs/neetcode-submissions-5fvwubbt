# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # check if lists is empty or not
        if len(lists) == 0:
            return None

        minHeap = []
        # add first item of each list to the heap
        for i in range((len(lists))):
            if lists[i]:
                heapq.heappush(minHeap,(lists[i].val,i,lists[i]))

        dummy = ListNode(0)
        cur = dummy
        
        # while the the number of lists are more than one
        while minHeap:
            val,index,node = heapq.heappop(minHeap)
            cur.next = node
            cur = cur.next
            # merge the lists 2 by 2
            # e.g [[2,6][1,8],[3,4]]
                    # [[1,2,6,8],[3,4]]
                    # [[1,2,3,4,6,8]]
            
            if node.next:
                node = node.next
                heapq.heappush(minHeap,(node.val,index,node))

        return dummy.next