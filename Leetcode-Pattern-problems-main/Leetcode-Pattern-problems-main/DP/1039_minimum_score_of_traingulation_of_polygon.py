class Solution:
    ''' RECURSION + MEMOIZATION 
    def solve(self,values,i,j,dp):
        if i+1==j:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        ans = float('inf')
        for k in range(i+1,j):
            ans = min(ans,values[i]*values[j]*values[k] +
                        self.solve(values,i,k,dp) +
                        self.solve(values,k,j,dp))
        dp[i][j] = ans 
        return dp[i][j]
    '''
    def solve(self,values,i,j):
        n = len(values)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i+2,n):
                ans = float('inf')
                for k in range(i+1,j):
                    ans = min(ans,values[i]*values[j]*values[k] +
                                dp[i][k] +
                                dp[k][j])
                dp[i][j] = ans 
        return dp[i][j]

    def minScoreTriangulation(self, values: list[int]) -> int:
        n = len(values)
        return self.solve(values,0,n-1)

obj = Solution()
values = [3,7,4,5]
print(obj.minScoreTriangulation(values))