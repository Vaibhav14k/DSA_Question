class Solution:
    def isMagicSquare(self, matrix):
        # Check if the 3x3 matrix contains all numbers from 1 to 9
        nums = set()
        for row in matrix:
            nums.update(row)
        if nums != set(range(1, 10)):
            return False
        
        MAGIC_CONSTANT = 15
        
        for row in matrix:
            if sum(row) != MAGIC_CONSTANT:
                return False
        
        for col in range(3):
            if sum(matrix[row][col] for row in range(3)) != MAGIC_CONSTANT:
                return False
        
        if sum(matrix[i][i] for i in range(3)) != MAGIC_CONSTANT:
            return False
        if sum(matrix[i][2-i] for i in range(3)) != MAGIC_CONSTANT:
            return False
        return True
    
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        if n < 3 or m < 3:
            return 0
        count = 0
        for i in range(n - 2):
            for j in range(m - 2):
                submatrix = [row[j:j+3] for row in grid[i:i+3]]
                if self.isMagicSquare(submatrix):
                    count += 1
        return count


obj = Solution()
grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
print(obj.numMagicSquaresInside(grid)) 