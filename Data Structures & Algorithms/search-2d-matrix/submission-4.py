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
