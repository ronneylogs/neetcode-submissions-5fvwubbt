class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowLeft,rowRight = 0,len(matrix) - 1
        foundRow = 0
        
        while rowLeft<=rowRight:
            mid = (rowLeft + rowRight) // 2
            if target < matrix[mid][0]:
                rowRight = mid - 1
            elif target > matrix[mid][-1]:
                rowLeft = mid + 1
            else:
                foundRow = mid
                break
            
        colLeft,colRight = 0,len(matrix[foundRow])-1

        while colLeft<=colRight:
            mid = (colLeft + colRight) // 2
            if target == matrix[foundRow][mid]:
                return True
            elif target > matrix[foundRow][mid]:
                colLeft = mid + 1
            else:
                colRight = mid - 1
        
        return False
        


    

    # Inputs = [[1,2,3],[4,5,6],[7,8,9]], target = 6

    # Output = true or false


    # Idea:
    # Perform binary search on the row first then do it by column

    # Binary search on the row:
    # if target less than first number then move right pointer
    # if target greater than last number then move left pointer
    # otherwise we found the row, bingo!


    # Structure
    # Two separate binary searches