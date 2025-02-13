class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # Time: O(nm)
        # Space: O(nm)
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                i = matrix[r][c] + \
                    (matrix[r][c - 1] if c != 0 else 0) + \
                    (matrix[r - 1][c] if r != 0 else 0) - \
                    (matrix[r - 1][c - 1] if r != 0 and c != 0 else 0)
                matrix[r][c] = i
        self.matrix = matrix
            
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Time: O(1)
        # Space: O(1)
        return (self.matrix[row2][col2]) - \
               (self.matrix[row2][col1 - 1] if col1 != 0 else 0) - \
               (self.matrix[row1 - 1][col2] if row1 != 0 else 0) + \
               (self.matrix[row1 - 1][col1 - 1] if row1 != 0 and col1 != 0 else 0)

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)