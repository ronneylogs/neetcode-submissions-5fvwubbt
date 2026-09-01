class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0

        r = len(matrix) - 1
        row = 0

        while l<=r:
            m = (l+r) // 2

            if matrix[m][0] <= target and matrix[m][-1] >= target:
                row = m
                break
            elif target > matrix[m][0]:
                l = m+1
            else:
                r = m-1
        
        l = 0
        r = len(matrix[0]) - 1
        
        while l<=r:
            m = (l+r) // 2

            if matrix[row][m] == target:
                return True
            elif matrix[row][m] < target:
                l = m+1
            else:
                r = m-1

        return False 



        # Idea
        # 1. Find the row that has the item
            # The first index should be smaller or equal    
            # The last index should be greater or equal 
        # 2. Find the item in the row
            # regular binary search
