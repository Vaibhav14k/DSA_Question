class Solution:
    ''' RECURSION + MEMOIZATION
    def solve(self,matrix,maxx,i,j,dp):
        if (i>=len(matrix) or j>=len(matrix[0])):
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        diagonal = self.solve(matrix,maxx,i+1,j+1,dp)
        bottom = self.solve(matrix,maxx,i+1,j,dp)
        right = self.solve(matrix,maxx,i,j+1,dp)
        if matrix[i][j] == "1":
            dp[i][j] = 1 + min(diagonal,min(bottom,right))
            maxx[0] = max(dp[i][j],maxx[0])
            return dp[i][j] 
        else:
            dp[i][j]=0 
            return dp[i][j]
    '''
    ''' TABULAR METHOD
    def solve(self,matrix,maxx,i,j):
        row = len(matrix)
        col = len(matrix[0])
        dp = [[0 for _ in range(col + 1)] for _ in range(row + 1)]
        for i in range(row-1,-1,-1):
            for j in range(col-1,-1,-1):
                right = dp[i][j+1]
                bottom = dp[i+1][j]
                diagonal = dp[i+1][j+1]
                if matrix[i][j] == "1":
                    dp[i][j] = 1 + min(diagonal,min(bottom,right))
                    maxx[0] = max(dp[i][j],maxx[0])
                else:
                    dp[i][j]=0
        else:
            dp[i][j]=0 
        return dp[i][j]
    '''
    def solve(self,matrix,maxx,i,j):
        row = len(matrix)
        col = len(matrix[0])
        current = [0] * (col+1)
        previous = [0] * (col+1)
        for i in range(row-1,-1,-1):
            for j in range(col-1,-1,-1):
                right = current[j+1]
                bottom = previous[j]
                diagonal = previous[j+1]
                if matrix[i][j] == "1":
                    current[j] = 1 + min(diagonal,min(bottom,right))
                    maxx[0] = max(current[j],maxx[0])
                else:
                    current[j]=0
            previous = current[:]
        return current[j]
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        maxx = [0]
        self.solve(matrix,maxx ,0,0)
        return maxx[0] * maxx[0]

obj = Solution()
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(obj.maximalSquare(matrix))