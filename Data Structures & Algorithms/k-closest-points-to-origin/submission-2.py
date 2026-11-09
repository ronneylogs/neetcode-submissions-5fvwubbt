class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        res = []

        for i in range(len(points)):
            value = math.sqrt((points[i][0] - 0)**2 + (points[i][1] - 0)**2)
            heapq.heappush(arr,((value,points[i])))

        for i in range(k):
            res.append(heapq.heappop(arr)[1])
        

        return res





        # Use a heap
        # Use Euclidean distance (sqrt((x1 - x2)^2 + (y1 - y2)^2))
        # 1. create an array to store our points
        # 2. go through the points, and add each point to the heap
        # 3. at the end pop out k points
        

        # [[0,2],[2,2]], k = 1

