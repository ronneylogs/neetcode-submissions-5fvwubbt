class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Find row
        l = 0
        r = len(matrix) - 1
    
        foundRow = 0
        while l<=r:
            m = (l+r) // 2

            if matrix[m][0] <= target and matrix[m][-1] >= target:
                foundRow = m
                break
    
            if matrix[m][0] > target:
                r = m-1
            else:
                l = m+1
            

        l = 0
        r = len(matrix[0]) - 1

        while l<=r:
            m = (l+r) // 2

            if target == matrix[foundRow][m]:
                return True
            
            if matrix[foundRow][m] > target:
                r = m - 1
            else:
                l = m + 1
        
        return False

        





        # Intuition
            # Find the row that has the answer then find the answer within the row


        # Algorithm
            # Use binary search to find the row that has the answer
                # the right answer should have the first index <target and last index > target
                # l=m+1, when target>row last item
                # r=m-1, when target<row first item

            # Use regular binary search on the found row to get answer
        