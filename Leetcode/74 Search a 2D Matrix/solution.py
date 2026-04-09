class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        colomn = len(matrix[0])
        left = 0
        right = row * colomn - 1

        while left <= right:
            mid = (left + right) // 2
            r = mid // colomn
            c = mid % colomn
            if matrix[r][c] == target:
                return True
            
            if matrix[r][c] > target:
                right = mid - 1

            else:
                left = mid + 1
        
        return False
        



            