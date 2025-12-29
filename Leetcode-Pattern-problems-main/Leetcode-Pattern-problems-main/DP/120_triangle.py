class Solution:
    ''' RECURSION + MEMOIZATION
    def solve(self,triangle,row,i,dp):
        if i==len(triangle[row]):
            return 0
        if row==len(triangle)-1:
            return triangle[row][i]
        elif dp[row][i] != -1:
            return dp[row][i]
        else:
            dp[row][i] = triangle[row][i]+min(self.solve(triangle,row+1,i,dp),self.solve(triangle,row+1,i+1,dp))
            return dp[row][i]

    def minimumTotal(self, triangle: list[list[int]]) -> int:
        dp = [[-1 for _ in range(len(triangle[-1]))] for _ in range(len(triangle))]
        return self.solve(triangle,0,0,dp)
    '''
    def solve(self,triangle):
        curr = [0] * (len(triangle[-1])+1)
        next = [0] * (len(triangle[-1])+1)
        for row in range(len(triangle)-1,-1,-1):
            for i in range(len(triangle[row])-1,-1,-1):
                curr[i] = triangle[row][i]+min(next[i],next[i+1])
            next = curr[:]
        return next[0]

    def minimumTotal(self, triangle: list[list[int]]) -> int:
        return self.solve(triangle)

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(Solution().minimumTotal(triangle))