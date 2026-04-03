class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        for i in nums:
            maxHeap.append([-i,i])
        heapq.heapify(maxHeap)
        

        while k>1:
            heapq.heappop(maxHeap)
            k = k - 1

        return heapq.heappop(maxHeap)[1]


# def findKthLargest(self, nums, k):
#         return heapq.nlargest(k, nums)[-1]

        


        # idea
        # create a maxHeap by adding negative to all the numbers