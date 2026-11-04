class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k

        self.arr = nums

        heapq.heapify(self.arr)

        while len(self.arr) > k:
            heapq.heappop(self.arr)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.arr,val)

        if len(self.arr) > self.k:
            heapq.heappop(self.arr)
        
        return self.arr[0]
        

# # init
# - create an array to track of nums
# - heapify the elemetn inside of nums

# - create a k to keep track of k


# # add
# - add the item to the heap
# - if the len item is greater than k, remove one item from the heap
# - return the last item in the heap